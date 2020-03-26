
#

# Test cases example for lab 1.

#

# Name:Hayden

# Section:05

#


import unittest      # import the module that supports writing unit tests



# Define a class that will be used for these test cases.

# This class will include testing functions.

#

# Much of this code should be viewed as boilerplate for now.

#

class TestsLab1(unittest.TestCase):

   def test_expressions(self):         # Defines one testing function.

      self.assertEqual(0 + 1, 1)

      # Add code here (like the line above) for the additional test cases.


	
      self.assertEqual(2 * 2, 4)
	
      self.assertEqual(19//3,6)  #Python3 rounds down to nearest whole number, like floor due to "//"
     
      self.assertAlmostEqual(19/3, 6.3333333) #Python3 outputs float while Python outputs int 

      self.assertAlmostEqual(19/3.0, 6.333333333333333)   #Python3 & Python ouptut float cuz of float val

      self.assertAlmostEqual(19.0/3.0, 6.3333333333)        #Python3 outputs float
      
      self.assertEqual(4*2+27//3+4, 21)                    

      self.assertEqual(4*(2+27)//3+4, 42)              #outputs whole number because of "//"


# Run the unit tests.

if __name__ == '__main__':

   unittest.main()
