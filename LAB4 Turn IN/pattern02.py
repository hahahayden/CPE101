# Lab 4
#
# Name:Hayden Tam
# Instructor: Sussan Einakian
# Section:05
import driver

#Purpose: take an input for the pattern02 and checks if each row and column has the same letter; R is half and Q is the other half horizontally
#int,int-> string

def letter(row, col):
   if (row <=9):
      return 'R'
   else:
      return 'Q'
if __name__ == '__main__':
        driver.comparePatterns(letter)





