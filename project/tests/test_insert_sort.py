from coe_number_.insert_sort import insertion_sort
import unittest

class SortTest(unittest.TestCase):
    def test_data(self):
        data = [-2643, 16, 984, -28, 251, 3450, -325]
        insertion_sort(data)
        for i in data:
            print(i, end=" ")
        print(" ")
        