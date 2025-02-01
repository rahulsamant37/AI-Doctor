import elevenlabs
from elevenlabs.client import ElevenLabs
from config.settings import settings

class ElevenLabsClient:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
    
    def text_to_speech(self, text, output_path):
        audio = self.client.generate(
            text=text,
            voice=settings.TTS_VOICE,
            model=settings.TTS_MODEL
        )
        elevenlabs.save(audio, output_path)
        return output_path