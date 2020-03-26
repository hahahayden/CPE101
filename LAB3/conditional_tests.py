# Lab 3
#
# Name:Hayden Tam 
# Instructor: Sussan Einakian
# Section: 5
import unittest
import conditional

class TestCases(unittest.TestCase):
   def test_case(self):
      # Add code here.
      self.assertEqual(conditional.max_101(2,3),3)
      self.assertEqual(conditional.max_101(4,3),4)
      self.assertEqual(conditional.max_101(5,6),6)
      self.assertEqual(conditional.max_of_three(4,7,8),8)
      self.assertEqual(conditional.max_of_three(9,4,6),9)
      
      self.assertEqual(conditional.max_of_three(2,3,4),4)
      self.assertEqual(conditional.rental_late_fee(10),7)
      self.assertEqual(conditional.rental_late_fee(24),19)
      self.assertEqual(conditional.rental_late_fee(50),100)
# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

