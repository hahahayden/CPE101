# Lab 4
#
# Name:Hayden Tam
# Instructor: Sussan Einakian
# Section:05

import driver
#Purpose: take an input for the pattern05 and checks if each row and column has the same letter; T on lower triangle W on upper triangle
#int,int-> string

def letter(row, col):
   if (0<=row<=col and 0<=col<=20):
      
      
      return 'W'
   else:
      
      return 'T'
if __name__ == '__main__':
        driver.comparePatterns(letter)









