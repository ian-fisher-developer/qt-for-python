import unittest
import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_greeting(self):
        self.assertEqual(hello_world.greeting(), 'Hello Qt for Python!')


if __name__ == '__main__':
    unittest.main()
