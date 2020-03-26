# Lab 4
#
# Name:Hayden Tam
# Instructor: Sussan Einakian
# Section:05
#Purpose: take an input for the pattern04 and checks if each row and column has the same letter; M is in the middle of S        
#int,int-> string

import driver
def letter(row, col):
   if( (2<=row<=4)and (3<=col<=6)):
      return 'M'
   else:
      return 'S'
if __name__ == '__main__':
        driver.comparePatterns(letter)





