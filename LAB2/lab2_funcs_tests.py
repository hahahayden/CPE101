#Lab 2 Test Cases
#Name: Hayden Tam
#Section:05
import unittest
import funcs

class TestCases(unittest.TestCase):
   def test_math_func1(self):
      self.assertAlmostEqual(funcs.math_func1(1,1),.16666666)
      self.assertEqual(funcs.math_func1(0,0),0)
      pass


   def test_math_func2(self):
      self.assertAlmostEqual(funcs.math_func2(1,4,4),-2)
      self.assertAlmostEqual(funcs.math_func2(1,6,9),-3)
      pass

   def test_d(self):
     self.assertEqual(funcs.d(4,0,0,0),4)
     self.assertEqual(funcs.d(2,0,2,0),0)    
     pass
      
   def test_is_negative(self):
     self.assertEqual(funcs.is_negative(-4),True)
     self.assertEqual(funcs.is_negative(8),False)
     pass

   def test_dividable_by_5(self):
     self.assertEqual(funcs.dividable_by_5(15),True)
     self.assertEqual(funcs.dividable_by_5(14),False)
     pass

# Run the unit tests.
if __name__ == '__main__':
     unittest.main()

