#Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05
import unittest
import map

class TestCases(unittest.TestCase):
    list=[-5,-8,2,3,6,7,8]
    list2=[-5,2,4,6,-7,9]
    def test_are_positive(self):
       self.assertEqual(map.are_positive([-5,-8,2,3,6,7,8]),[2,3,6,7,8] )
       self.assertEqual(map.are_positive([-5,2,4,6,-7,9]),[2,4,6,9])

    def test_are_divisible_by_n(self):
        self.assertEqual(map.are_divisible_by_n([-5,-8,2,3,6,7,8],2),[-8,2,6,8])
        self.assertEqual(map.are_divisible_by_n([-5,2,4,6,-7,9],3),[6,9])
    def test_are_greater_than_n(self):
        self.assertEqual(map.are_greater_than_n([-5,-8,2,3,6,7,8],2),[3,6,7,8])
        self.assertEqual(map.are_greater_than_n([-5,2,4,6,-7,9],5),[6,9])
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

