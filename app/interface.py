import gradio as gr
from config.settings import settings
from services import GroqClient, ElevenLabsClient
from utils.image_processor import encode_image

class DoctorInterface:
    def __init__(self):
        self.groq_client = GroqClient()
        self.tts_client = ElevenLabsClient()
    
    def process_inputs(self, audio_path, image_path):
        # Speech to text
        user_query = self.groq_client.transcribe_audio(audio_path)
        
        # Image analysis
        if image_path:
            encoded_image = encode_image(image_path)
            full_query = settings.SYSTEM_PROMPT + user_query
            diagnosis = self.groq_client.analyze_image(full_query, encoded_image)
        else:
            diagnosis = "No image provided for analysis."
        
        # Generate audio response
        output_path = "diagnosis_response.mp3"
        self.tts_client.text_to_speech(diagnosis, output_path)
        
        return user_query, diagnosis, output_path
    
    def launch(self):
        iface = gr.Interface(
            fn=self.process_inputs,
            inputs=[
                gr.Audio(sources=["microphone"], type="filepath", label="Input Audio"),
                gr.Image(type="filepath", label="Input Image")
            ],
            outputs=[
                gr.Textbox(label="User Query"),
                gr.Textbox(label="Educational Analysis"),
                gr.Audio(label="Audio Response")
            ],
            title="Medical Image Education Assistant",
            description="""This is an educational tool to help learn about medical imaging concepts.
            NOT for medical diagnosis. Always consult healthcare professionals for medical advice."""
        )
        iface.launch()