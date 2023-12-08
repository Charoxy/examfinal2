import unittest

class TestStringMethods(unittest.TestCase):

    def test_fizz(self):
        self.assertTrue(3%3 == 0)
        self.assertFalse(4%3 == 0)

    def test_buzz(self):
        self.assertTrue(10%5 == 0)
        self.assertFalse(4%5 == 0)

    def test_fizzBuzz(self):
        self.assertTrue(15%3 == 0 and 15%5 == 0)
        self.assertFalse(4%3 == 0 and 4%5 == 0)


if __name__ == '__main__':
    unittest.main()
