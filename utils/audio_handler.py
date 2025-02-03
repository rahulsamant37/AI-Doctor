from typing import Dict, Union
import os

class AudioProcessingError(Exception):
    """Custom exception for audio processing errors"""
    pass

def process_audio(file_path: str) -> Dict[str, Union[bool, str, float]]:
    """
    Process an audio file and return metadata and processing status.
    
    Args:
        file_path (str): Path to the audio file
        
    Returns:
        dict: Dictionary containing processing results
            {
                'processed': bool,
                'format': str,
                'duration': float,
                'sample_rate': int
            }
            
    Raises:
        FileNotFoundError: If the audio file doesn't exist
        AudioProcessingError: If there's an error processing the audio
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
        
    if not file_path.endswith(('.wav', '.mp3', '.m4a')):
        raise AudioProcessingError(f"Unsupported audio format: {file_path}")

    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        raise AudioProcessingError("Empty audio file")
    if file_size > 50_000_000:  # 50MB limit
        raise AudioProcessingError("Audio file too large")
        
    # Basic file header validation
    with open(file_path, 'rb') as f:
        header = f.read(4)
        if file_path.endswith('.wav'):
            if header != b'RIFF':
                raise AudioProcessingError("Invalid or corrupted WAV file")
        elif file_path.endswith('.mp3'):
            if not (header.startswith(b'\xFF\xFB') or header.startswith(b'\xFF\xF3')):
                raise AudioProcessingError("Invalid or corrupted MP3 file")
        elif file_path.endswith('.m4a'):
            if not (header.startswith(b'ftyp') or header.startswith(b'\x00\x00\x00')):
                raise AudioProcessingError("Invalid or corrupted M4A file")
    
    # Dummy implementation - in real code, this would actually process the audio
    return {
        'processed': True,
        'format': os.path.splitext(file_path)[1][1:],
        'duration': 10.5,
        'sample_rate': 44100
    }

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe speech from an audio file to text.
    
    Args:
        file_path (str): Path to the audio file
        
    Returns:
        str: Transcribed text from the audio
        
    Raises:
        FileNotFoundError: If the audio file doesn't exist
        AudioProcessingError: If there's an error transcribing the audio
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
        
    if not file_path.endswith(('.wav', '.mp3', '.m4a')):
        raise AudioProcessingError(f"Unsupported audio format for transcription: {file_path}")
    
    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size == 0:
        raise AudioProcessingError("Empty audio file")
    if file_size > 50_000_000:  # 50MB limit
        raise AudioProcessingError("Audio file too large")

    # Basic file validation (reusing code from process_audio)
    with open(file_path, 'rb') as f:
        header = f.read(4)
        if file_path.endswith('.wav'):
            if header != b'RIFF':
                raise AudioProcessingError("Invalid or corrupted WAV file")
        elif file_path.endswith('.mp3'):
            if not (header.startswith(b'\xFF\xFB') or header.startswith(b'\xFF\xF3')):
                raise AudioProcessingError("Invalid or corrupted MP3 file")
        elif file_path.endswith('.m4a'):
            if not (header.startswith(b'ftyp') or header.startswith(b'\x00\x00\x00')):
                raise AudioProcessingError("Invalid or corrupted M4A file")
    
    # Dummy implementation - in real code, this would use a speech recognition service
    return "This is a simulated transcription of the audio file."