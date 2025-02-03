# AI-Doctor

An AI-powered medical diagnostic assistant that processes audio queries and medical images to provide preliminary medical insights.

![AI-Doctor Interface](https://github.com/rahulsamant37/AI-Doctor/blob/main/assets/healthcare.png)

## ✨ Key Features

-  Voice-based interaction for medical queries
-  Medical image analysis 
-  Text-to-Speech response generation
-  Support for multiple audio formats (WAV, MP3, M4A)
-  Intuitive web interface using Gradio

## 🛠️ Tech Stack

-  Python 3.12
-  Groq AI for image analysis and speech recognition
-  ElevenLabs for text-to-speech
-  Gradio for web interface
-  Docker for containerization
-  GitHub Actions for CI/CD

## 📁 Project Structure

```
ai-doctor/
├── 📱 app/
│   ├── __init__.py
│   ├── main.py
│   └── interface.py
├── ⚙️ config/
│   ├── __init__.py
│   └── settings.py
├── 🔌 services/
│   ├── __init__.py
│   ├── groq_client.py
│   └── elevenlabs_client.py
├── 🔧 utils/
│   ├── __init__.py
│   ├── audio_handler.py
│   └── image_processor.py
├── 🧪 tests/
│   ├── __init__.py
│   ├── test_audio_handler.py
│   └── test_image_processor.py
├── .env
├── .gitignore
├── 🐳 Dockerfile
├── 📝 requirements.txt
└── 📖 README.md
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-doctor.git
cd ai-doctor
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Linux/Mac
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
# Create .env file with your API keys
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## 💻 Usage

1. Start the application:
```bash
python app/main.py
```

2. Open your browser and navigate to:
```
http://localhost:7860
```

3. Use the interface to:
   - 🎤 Record or upload audio queries
   - 📸 Upload medical images for analysis
   - 🔊 Receive audio and text responses

## 🎯 Sample Output
<div align="center">

![AI-Doctor Sample Output](https://github.com/rahulsamant37/AI-Doctor/blob/main/assets/output.png)

*Example of AI-Doctor analyzing a medical image and providing diagnosis suggestions*

</div>

## 👨‍💻 Development

###  Running Tests
```bash
pytest
```

### Docker Build
```bash
# Build Docker image
docker build -t ai-doctor .

# Run container
docker run -p 7860:7860 ai-doctor
```

### 🔄 CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment.

On push/PR to main:
-  Runs tests
-  Builds Docker image
-  Pushes to Docker Hub

Requirements:
- Add Docker Hub credentials to repository secrets:
  - `DOCKER_USERNAME`
  - `DOCKER_PASSWORD`

## 📚 API Documentation

### Audio Processing
- Supported formats: WAV, MP3, M4A
- Maximum file size: 50MB
- Sample rates: 8000, 16000, 44100, 48000 Hz

### Image Processing
- Supported formats: PNG, JPEG
- Base64 encoding for API transmission

## 📜 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1.  Fork the repository
2.  Create feature branch (`git checkout -b feature/name`)
3.  Commit changes (`git commit -am 'Add feature'`)
4.  Push branch (`git push origin feature/name`)
5.  Create Pull Request

## 👥 Authors

Your Name ([@rahulsamant37](https://github.com/rahulsamant37))

## 🙏 Acknowledgments

- 🧠 Groq AI for machine learning capabilities
- 🗣️ ElevenLabs for text-to-speech services
- 🎨 Gradio for the web interface framework

---
Note: This is a diagnostic assistance tool and should not be used as a replacement for professional medical diagnosis. Always consult qualified healthcare providers for medical decisions.
