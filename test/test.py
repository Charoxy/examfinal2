import unittest

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

class TestStringMethods(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzBuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_none(self):
        self.assertEqual(fizzbuzz(7), "7")


if __name__ == '__main__':
    unittest.main()
