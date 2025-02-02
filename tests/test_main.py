import unittest
from src.main import hello_world


class TestHelloWorld(unittest.TestCase):
    def test_hello_word_passing(self):
        self.assertEqual(hello_world(), 1)

    def test_hello_word_failing(self):
        self.assertEqual(hello_world(), 2)


if __name__ == "__main__":
    unittest.main()
