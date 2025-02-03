import unittest
import os
from utils.audio_handler import process_audio, transcribe_audio, AudioProcessingError

class TestAudioHandler(unittest.TestCase):
    def setUp(self):
        """Set up test files with minimal valid audio file headers"""
        self.test_files = {
            'wav': 'test_audio.wav',
            'mp3': 'test_audio.mp3',
            'txt': 'test_audio.txt'
        }
        
        # Create a minimal valid WAV file header
        wav_header = (
            b'RIFF'    # ChunkID
            b'\x24\x00\x00\x00'  # ChunkSize (36 bytes)
            b'WAVE'    # Format
            b'fmt '    # Subchunk1ID
            b'\x10\x00\x00\x00'  # Subchunk1Size (16 bytes)
            b'\x01\x00'  # AudioFormat (PCM)
            b'\x01\x00'  # NumChannels (1)
            b'\x44\xAC\x00\x00'  # SampleRate (44100)
            b'\x88\x58\x01\x00'  # ByteRate
            b'\x02\x00'  # BlockAlign
            b'\x10\x00'  # BitsPerSample (16)
            b'data'    # Subchunk2ID
            b'\x00\x00\x00\x00'  # Subchunk2Size (0 bytes of audio data)
        )
        
        # Write the test files
        with open(self.test_files['wav'], 'wb') as f:
            f.write(wav_header)
        
        # Create a minimal MP3 file header
        mp3_header = b'\xFF\xFB\x90\x64'  # MPEG-1 Layer 3, 128 kbps
        with open(self.test_files['mp3'], 'wb') as f:
            f.write(mp3_header)
            
        # Create empty text file
        with open(self.test_files['txt'], 'wb') as f:
            f.write(b'')

    def tearDown(self):
        # Clean up test files
        for file_path in self.test_files.values():
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_process_audio_valid_wav(self):
        result = process_audio(self.test_files['wav'])
        self.assertTrue(result['processed'])
        self.assertEqual(result['format'], 'wav')
        self.assertIsInstance(result['duration'], float)
        self.assertIsInstance(result['sample_rate'], int)

    def test_process_audio_valid_mp3(self):
        result = process_audio(self.test_files['mp3'])
        self.assertTrue(result['processed'])
        self.assertEqual(result['format'], 'mp3')

    def test_process_audio_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            process_audio("non_existent_audio.wav")

    def test_process_audio_invalid_format(self):
        with self.assertRaises(AudioProcessingError):
            process_audio(self.test_files['txt'])

    def test_transcribe_audio_valid_wav(self):
        transcription = transcribe_audio(self.test_files['wav'])
        self.assertIsInstance(transcription, str)
        self.assertTrue(len(transcription) > 0)

    def test_transcribe_audio_valid_mp3(self):
        transcription = transcribe_audio(self.test_files['mp3'])
        self.assertIsInstance(transcription, str)
        self.assertTrue(len(transcription) > 0)

    def test_transcribe_audio_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            transcribe_audio("non_existent_audio.wav")

    def test_transcribe_audio_invalid_format(self):
        with self.assertRaises(AudioProcessingError):
            transcribe_audio(self.test_files['txt'])
    
    def test_process_audio_metadata_ranges(self):
        """Test that audio metadata falls within expected ranges"""
        result = process_audio(self.test_files['wav'])
        self.assertGreater(result['duration'], 0)
        self.assertLess(result['duration'], 3600)  # Assume max 1 hour
        self.assertIn(result['sample_rate'], [8000, 16000, 44100, 48000])  # Common rates

    def test_transcribe_audio_non_empty_output(self):
        """Test that transcription output is meaningful"""
        result = transcribe_audio(self.test_files['wav'])
        self.assertNotEqual(result.strip(), "")
        self.assertGreater(len(result.split()), 1)  # At least 2 words
    
    def test_process_audio_empty_file(self):
        """Test handling of empty audio files"""
        with open(self.test_files['wav'], 'wb') as f:
            f.write(b'')
        with self.assertRaises(AudioProcessingError):
            process_audio(self.test_files['wav'])

    def test_process_audio_corrupted_file(self):
        """Test handling of corrupted audio files"""
        # Create a corrupted audio file
        with open(self.test_files['wav'], 'wb') as f:
            f.write(b'corrupted_content')
        with self.assertRaises(AudioProcessingError):
            process_audio(self.test_files['wav'])

    def test_transcribe_audio_max_size(self):
        """Test handling of oversized audio files"""
        # Create a large dummy file (e.g., 100MB)
        with open(self.test_files['wav'], 'wb') as f:
            f.write(b'0' * 100_000_000)
        with self.assertRaises(AudioProcessingError):
            transcribe_audio(self.test_files['wav'])

    def test_supported_formats(self):
        """Test all supported audio formats"""
        # Define headers for each format
        format_headers = {
            '.wav': (
                b'RIFF'    # ChunkID
                b'\x24\x00\x00\x00'  # ChunkSize (36 bytes)
                b'WAVE'    # Format
                b'fmt '    # Subchunk1ID
                b'\x10\x00\x00\x00'  # Subchunk1Size (16 bytes)
                b'\x01\x00'  # AudioFormat (PCM)
                b'\x01\x00'  # NumChannels (1)
                b'\x44\xAC\x00\x00'  # SampleRate (44100)
                b'\x88\x58\x01\x00'  # ByteRate
                b'\x02\x00'  # BlockAlign
                b'\x10\x00'  # BitsPerSample (16)
                b'data'    # Subchunk2ID
                b'\x00\x00\x00\x00'  # Subchunk2Size
            ),
            '.mp3': b'\xFF\xFB\x90\x64',  # MPEG-1 Layer 3, 128 kbps
            '.m4a': b'ftyp'  # Basic M4A header
        }
        
        for fmt in format_headers:
            test_file = f'test_audio{fmt}'
            try:
                with open(test_file, 'wb') as f:
                    f.write(format_headers[fmt])
                result = process_audio(test_file)
                self.assertTrue(result['processed'])
                self.assertEqual(result['format'], fmt[1:])
            finally:
                if os.path.exists(test_file):
                    os.remove(test_file)

if __name__ == "__main__":
    unittest.main()