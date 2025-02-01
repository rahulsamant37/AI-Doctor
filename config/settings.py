from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    
    # Model configurations
    VISION_MODEL = "llama-3.2-90b-vision-preview"
    STT_MODEL = "whisper-large-v3"
    TTS_VOICE = "Aria"
    TTS_MODEL = "eleven_turbo_v2"
    
    SYSTEM_PROMPT = """You have to act as a professional doctor... [truncated for brevity]"""

settings = Settings()