import unittest
from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_english_to_french(self):
        self.assertNotEqual(english_to_french(0), 0)
        self.assertNotEqual(english_to_french('None'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french("How are you today?"), "Comment es-tu aujourd'hui?")

    def test_french_to_english(self):
        self.assertNotEqual(french_to_english(0), 0)
        self.assertNotEqual(french_to_english('None'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english("Comment es-tu aujourd'hui?"), "How are you today?")

if __name__=='__main__':
    unittest.main() 
