import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_is_lower_than_101(self):
      self.assertEqual(is_lower_101("b"),True)
      self.assertEqual(is_lower_101("C"),False)
      

   def test_char_rot13(self):
      self.assertEqual(char_rot13("a"),"n")
      self.assertEqual(char_rot13("A"),"N")
      self.assertEqual(char_rot13("N"),"A")
      
if __name__ == '__main__':
   unittest.main()

