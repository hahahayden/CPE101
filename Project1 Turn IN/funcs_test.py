# Project1
# 
# Name: Hayden Tam
# Instructor: S. Einakian
# Section:05

import unittest
import funcs

class TestCases(unittest.TestCase):
    def test_poundsToKG(self):
        self.assertEqual(funcs.poundsToKG(100),45.3592)
        self.assertEqual(funcs.poundsToKG(140),63.50288)
                
    def test_getMassObject(self):
        self.assertEqual(funcs.getMassObject('t'),.1)
        self.assertEqual(funcs.getMassObject('p'),1.0)
        self.assertEqual(funcs.getMassObject('r'),3.0)
        self.assertEqual(funcs.getMassObject('g'),5.3)
        self.assertEqual(funcs.getMassObject('l'),9.07)
        
    def test_getVelocityObject(self):
        self.assertEqual(funcs.getVelocityObject(10),7)
        self.assertAlmostEqual(funcs.getVelocityObject(20),9.8994949)
    
    def test_getVelocitySkater(self):
        #test with tomato mass
        
        self.assertEqual(funcs.getVelocitySkater(100,.1,7),.007)
        self.assertEqual(funcs.getVelocitySkater(140,.1,9.899),.007)
        
        #test with banana cream pie mass
        
        self.assertEqual(funcs.getVelocitySkater(100,1.0,7),.07)
        self.assertEqual(funcs.getVelocitySkater(140,1.0,9.899),.071)

        #test with rock
        
        self.assertEqual(funcs.getVelocitySkater(100,3.0,7),.21)
        self.assertEqual(funcs.getVelocitySkater(140,3.0,9.899),.212)

        #test with gnome

        self.assertEqual(funcs.getVelocitySkater(100,5.3,7),.371)
        self.assertEqual(funcs.getVelocitySkater(140,5.3,9.899),0.375)

        #test with lightsaber
        
        self.assertEqual(funcs.getVelocitySkater(100,9.03,7),.632)
        self.assertEqual(funcs.getVelocitySkater(140,9.03,9.899),.638)
        
  # Run the unit tests.

if __name__ == '__main__':
     unittest.main()
  
