#Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05
import unittest
import filter

class TestCases(unittest.TestCase):
    def test_1(self):
       self.assertEqual(filter.square_all([1,2,3]),[1,4,9])
       self.assertEqual(filter.square_all([2,4,5]),[4,16,25])
    def test_2(self):
       self.assertEqual(filter.add_n_all(2,[1,2,3]),[3,4,5])
       self.assertEqual(filter.add_n_all(3,[1,2,3]),[4,5,6])
    def test_3(self):
       self.assertEqual(filter.even_or_odd_all([2,4,5,8]),[True,True,False,True])
       self.assertEqual(filter.even_or_odd_all([2,4,5,7]),[True,True,False,False])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

