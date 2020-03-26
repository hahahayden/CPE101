# Lab 3
#
# Name: Hayden Tam 
# Instructor: Sussan Einakian
# Section: 05
import unittest
import logic

class TestCases(unittest.TestCase):
   def test_case(self):
      # Add code here.
      self.assertEqual(logic.is_even(2),True)
      self.assertEqual(logic.is_even(5),False)
      self.assertEqual(logic.is_even(6),True)

      self.assertEqual(logic.in_an_interval(-10),False)
      self.assertEqual(logic.in_an_interval(0),True)
      self.assertEqual(logic.in_an_interval(9),False)
      self.assertEqual(logic.in_an_interval(20),True)
      self.assertEqual(logic.in_an_interval(120),True)
      self.assertEqual(logic.in_an_interval(127),True)


       


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

