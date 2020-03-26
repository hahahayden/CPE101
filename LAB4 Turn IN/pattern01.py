# Lab 4
#
# Name: Hayden Tam
# Instructor: Sussan Einakian
# Section: 05

import driver

#Purpose: take an input for the pattern01 and checks if each row and column has the same letter; Everywhere G but in the middle Z
#int,int-> string

def letter(row, col):
   if (row == 9 and col == 9):
      return 'Z'
   else:
      return 'G'
if __name__ == '__main__':
	driver.comparePatterns(letter)

