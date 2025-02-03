import unittest
import base64
import os
import io
from PIL import Image
from utils.image_processor import encode_image

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.test_image_path = "test_image.png"
        # Create a simple 1x1 transparent pixel PNG image
        img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
        img.save(self.test_image_path, format='PNG')

    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

    def test_encode_image(self):
        # Encode the image
        encoded_image = encode_image(self.test_image_path)
        
        # Verify the encoded string is valid base64
        decoded_data = base64.b64decode(encoded_image)
        
        # Try to open the decoded data as an image
        with Image.open(io.BytesIO(decoded_data)) as img:
            self.assertEqual(img.size, (1, 1))
            self.assertEqual(img.mode, 'RGBA')

    def test_encode_image_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            encode_image("non_existent_image.png")

if __name__ == "__main__":
    unittest.main()