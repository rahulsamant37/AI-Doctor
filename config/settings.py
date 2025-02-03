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
    
    SYSTEM_PROMPT = """As an educational AI assistant trained to analyze medical images for learning purposes:
        1. Describe what you observe in the image in detail
        2. Explain the general visual characteristics 
        3. Discuss common related medical concepts for educational purposes
        4. Suggest general wellness tips related to the topic
        
        Important: This is for educational demonstration only. Always consult qualified healthcare providers for actual medical advice and diagnosis.
        
        Please analyze the image and respond conversationally but remember to stay educational rather than diagnostic."""

settings = Settings()