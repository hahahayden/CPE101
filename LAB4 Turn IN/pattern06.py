# Lab 4
#
# Name: Hayden Tam
# Instructor: Sussan Einakian
# Section: 05

import driver
#Purpose: take an input for the pattern06 and checks if each row and column has the same letter; Main diagonal is X and opposite; the others are O
#int,int-> string

def letter(row, col):
   
   if (row==col)or (col+row==6):
      

      return 'X'
   else:

      return 'O'
if __name__ == '__main__':
        driver.comparePatterns(letter)


