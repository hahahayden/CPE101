import unittest
from fold import *

class TestCases(unittest.TestCase):
   def test_fold(self):
      # Add code here.
      
      self.assertEqual(sum([1,2,3,[4,5]]),15)
      self.assertEqual(sum([2,3,4,[7,8]]),24)
   def test_index_of_smallest(self):
      self.assertEqual(index_of_smallest([1,2,3,4,5]),0)
      self.assertEqual(index_of_smallest([1,1,2,4]),0)
      self.assertEqual(index_of_smallest([]),-1)
      self.assertEqual(index_of_smallest([1,2,3,4,[-20,0]]),4)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

