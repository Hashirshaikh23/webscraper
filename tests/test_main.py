# tests/test_main.py
from main import extract_data_from_url
import unittest
from main import extract_data_from_url

class TestScraper(unittest.TestCase):
    def test_valid_url(self):
        result = extract_data_from_url("https://github.com")
        self.assertIn("url", result)
        self.assertEqual(result["url"], "https://github.com")
        self.assertIn("title", result)

if __name__ == '__main__':
    unittest.main()
