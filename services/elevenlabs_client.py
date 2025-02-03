import platform
import subprocess
import elevenlabs
from elevenlabs.client import ElevenLabs
from config.settings import settings

class ElevenLabsClient:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
    
    def text_to_speech(self, text, output_path):
        """
        Generate text-to-speech using settings from config
        """
        audio = self.client.generate(
            text=text,
            voice=settings.TTS_VOICE,
            model=settings.TTS_MODEL
        )
        elevenlabs.save(audio, output_path)
        return output_path
    
    def text_to_speech_with_elevenlabs(self, input_text, output_filepath):
        """
        Generate text-to-speech with specific settings and auto-play
        """
        # Use existing client instead of creating new one
        audio = self.client.generate(
            text=input_text,
            voice="Aria",
            output_format="mp3_22050_32",
            model="eleven_turbo_v2"
        )
        elevenlabs.save(audio, output_filepath)
        self._play_audio(output_filepath)
    
    def _play_audio(self, filepath):
        """
        Internal method to play audio file based on operating system
        """
        os_name = platform.system()
        try:
            if os_name == "Darwin":  # macOS
                subprocess.run(['afplay', filepath])
            elif os_name == "Windows":  # Windows
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{filepath}").PlaySync();'])
            elif os_name == "Linux":  # Linux
                subprocess.run(['aplay', filepath])  # Alternative: use 'mpg123' or 'ffplay'
            else:
                raise OSError("Unsupported operating system")
        except Exception as e:
            print(f"An error occurred while trying to play the audio: {e}")