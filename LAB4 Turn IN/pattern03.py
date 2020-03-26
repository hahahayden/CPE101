# Lab 4
#
# Name: Hayden Tam
# Instructor: Sussan Einakian
# Section:05
import driver

#Purpose: take an input for the pattern03 and checks if each row and column has the same letter; X on one half and O on the other half vertically
#int,int-> string

def letter(row, col):
   if (col<10):
      return 'X'
   else:
      return 'O'
if __name__ == '__main__':
        driver.comparePatterns(letter)





