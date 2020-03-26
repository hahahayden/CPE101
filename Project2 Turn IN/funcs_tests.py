# Project 2 - Moonlander
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
    def test_updateAcceleration(self):
        self.assertAlmostEqual(updateAcceleration(1.62,9),1.296)
        self.assertAlmostEqual(updateAcceleration(1.62,5),0)
        
    def test_updateAltitude(self):
        self.assertEqual(updateAltitude(60,50,1.62),110.81)
        self.assertEqual(updateAltitude(90,80,1.62),170.81)

    def test_updateVelocity(self):
        self.assertEqual(updateVelocity(90,1.62),91.62)
        self.assertEqual(updateVelocity(100,1.62),101.62)
   
    def test_updateFuel(self):
        self.assertEqual(updateFuel(60,8),52)
        self.assertEqual(updateFuel(40,9),31)
	      

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

