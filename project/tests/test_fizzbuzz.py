from coe_number.fizzbuzz import fizz_buzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        number = 3
        expected_result = "Fizz"
        result = fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_5_is_Buzz(self):
        number = 5
        expected_result = "Buzz"
        result = fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_30_is_fizzBuzz(self):
        number = 30
        expected_result = "FizzBuzz"
        result = fizz_buzz(number)
        self.assertEqual(result,expected_result)