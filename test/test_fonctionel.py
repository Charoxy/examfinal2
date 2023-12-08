import unittest
from unittest.mock import patch
from io import StringIO

def fizzbuzz_output():
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        for i in range(1, 101):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        return mock_stdout.getvalue()

class TestFizzBuzzFunctional(unittest.TestCase):

    def test_fizzbuzz_output(self):
        expected_output = "\n".join([
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
            "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz",
            "31", "32", "Fizz", "34", "Buzz", "Fizz", "37", "38", "Fizz", "Buzz", "41",
            "Fizz", "43", "44", "FizzBuzz", "46", "47", "Fizz", "49", "Buzz", "Fizz", "52",
            "53", "Fizz", "Buzz", "56", "Fizz", "58", "59", "FizzBuzz", "61", "62", "Fizz",
            "64", "Buzz", "Fizz", "67", "68", "Fizz", "Buzz", "71", "Fizz", "73", "74",
            "FizzBuzz", "76", "77", "Fizz", "79", "Buzz", "Fizz", "82", "83", "Fizz", "Buzz",
            "86", "Fizz", "88", "89", "FizzBuzz", "91", "92", "Fizz", "94", "Buzz", "Fizz",
            "97", "98", "Fizz", "Buzz"
        ]) + "\n"

        self.assertEqual(fizzbuzz_output(), expected_output)

    def test_fizz_in_output(self):
        self.assertIn("Fizz", fizzbuzz_output())

    def test_buzz_in_output(self):
        self.assertIn("Buzz", fizzbuzz_output())

    def test_fizzbuzz_in_output(self):
        self.assertIn("FizzBuzz", fizzbuzz_output())

if __name__ == '__main__':
    unittest.main()
