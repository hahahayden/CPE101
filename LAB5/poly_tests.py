#Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05
import unittest
import poly

class TestPoly(unittest.TestCase):
   #do not delete this part use this to comapre two list
   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_poly_add2(self):
      poly1=[2.3,4.7,1.0]
      poly2=[1.2,2.1,-3.2]
      self.assertListAlmostEqual(poly.poly_add2([1,2,3],[2,3,4]),[3,5,7])
      self.assertListAlmostEqual(poly.poly_add2([2,5,7],[2,3,4]),[4,8,11])
      self.assertListAlmostEqual(poly.poly_add2(poly1,poly2),[3.5,6.8,-2.2])
   def test_poly_mult2(self):
      self.assertListAlmostEqual(poly.poly_mult2([1,2,3],[2,3,4]),[2,7,16,17,12])
      self.assertListAlmostEqual(poly.poly_mult2([1,2,5],[2,3,4]),[2,7,20,23,20])
   # Add tests here

if __name__ == '__main__':
   unittest.main()
