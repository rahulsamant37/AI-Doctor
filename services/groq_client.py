from groq import Groq
from config.settings import settings

class GroqClient:
    def __init__(self):
        self.client = Groq(api_key=settings.GROQ_API_KEY)
    
    def analyze_image(self, query, encoded_image):
        messages = [{
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
            ]
        }]
        
        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model=settings.VISION_MODEL
        )
        return chat_completion.choices[0].message.content
    
    def transcribe_audio(self, audio_filepath):
        with open(audio_filepath, "rb") as audio_file:
            transcript = self.client.audio.transcriptions.create(
                file=audio_file,
                model=settings.STT_MODEL
            )
        return transcript.text