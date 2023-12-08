import unittest


class TestStringMethods(unittest.TestCase):

    def fizzbuzz(number):
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return str(number)

    def test_fizz(self):
        self.assertEqual(self.fizzbuzz(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(self.fizzbuzz(5), "Buzz")

    def test_fizzBuzz(self):
        self.assertEqual(self.fizzbuzz(15), "FizzBuzz")

    def test_fizzBuzz(self):
        self.assertEqual(self.fizzbuzz(7), "7")



if __name__ == '__main__':
    unittest.main()
