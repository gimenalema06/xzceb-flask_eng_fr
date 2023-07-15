import unittest
from machinetranslation.translator import english_to_french, french_to_english

class testingTranslators(unittest.TestCase):
    def test_english_to_french1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    def test_english_to_french2(self):
        self.assertEqual(english_to_french("Thank you"), "Merci")

    def test_french_to_english1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_french_to_english2(self):
        self.assertEqual(french_to_english("Merci"), "Thank you")

if __name__=="__main__":
    unittest.main()

