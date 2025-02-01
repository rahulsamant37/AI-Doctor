import os

def create_project_structure(base_path="."):
    structure = [
        ".env",
        "Dockerfile",
        "requirements.txt",
        "config/__init__.py",
        "config/settings.py",
        "services/__init__.py",
        "services/groq_client.py",
        "services/elevenlabs_client.py",
        "utils/__init__.py",
        "utils/image_processor.py",
        "utils/audio_handler.py",
        "app/__init__.py",
        "app/main.py",
        "app/interface.py",
        "tests/__init__.py",
        "tests/test_image_processor.py",
        "tests/test_audio_handler.py",
    ]
    
    for path in structure:
        full_path = os.path.join(base_path, path)
        if path.endswith("/"):
            os.makedirs(full_path, exist_ok=True)
        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "w") as f:
                pass  # Create an empty file

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")