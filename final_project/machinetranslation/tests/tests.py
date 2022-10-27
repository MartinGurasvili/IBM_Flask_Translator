# import translator
import unittest

class TestSum(unittest.TestCase):

    def test_null(self):
        self.assertEqual(english_to_french(), "", "null input not accounted for")
        self.assertEqual(french_to_english(), "", "null input not accounted for")

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour", "incorrect translation")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello", "incorrect translation")

if __name__ == '__main__':
    unittest.main()
    print("No errors")