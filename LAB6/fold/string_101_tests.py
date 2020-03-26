import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_str_rot_13(self):
        self.assertEqual(str_rot_13("abcdefghijkl"),("nopqrstuvwxy"))
        self.assertEqual(str_rot_13("hello"),("uryyb"))
        self.assertEqual(str_rot_13("HELLO"),"URYYB")
   def test_str_translate_101(self):
        self.assertEqual(str_translate_101('abacdefgh','a','x'), 'xbxcdefgh')
        self.assertEqual(str_translate_101('abbbdefgh','b','y'), 'ayyydefgh')

if __name__ == '__main__':
   unittest.main()

