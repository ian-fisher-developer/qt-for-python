import hello_world
import unittest


class TestHelloWorld(unittest.TestCase):

    def test_greeting_says_hello(self):
        self.assertEqual(hello_world.greeting(), 'Hello Qt for Python!')


if __name__ == '__main__':
    unittest.main(verbosity=2)
