from coe_number.super_fizzbuzz import super_fizz_buzz
import unittest

class SuperFizzBuzzTest(unittest.TestCase):
    def test_give_3_is_Fizz(self):
        number = 3
        expected_result = "Fizz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_5_is_Buzz(self):
        number = 5
        expected_result = "Buzz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_30_is_FizzBuzz(self):
        number = 30
        expected_result = "FizzBuzz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_9_is_FizzFizz(self):
        number = 9
        expected_result = "FizzFizz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_25_is_BuzzBuzz(self):
        number = 25
        expected_result = "BuzzBuzz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_225_is_FizzFizzBuzzBuzz(self):
        number = 225
        expected_result = "FizzFizzBuzzBuzz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_11_is_NoFizzBuzz(self):
        number = 11
        expected_result = "NoFizzBuzz"
        result = super_fizz_buzz(number)
        self.assertEqual(result,expected_result)