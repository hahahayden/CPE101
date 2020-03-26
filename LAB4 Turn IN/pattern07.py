# Lab 4
#
# Name:Hayden Tam
# Instructor: Sussan Einakian
# Section:05




import driver

#Purpose: take an input for the pattern04 and checks if each row and column has the same letter       
#int,int-> string
def letter(row, col):
    if ((1 < row < 4 ) and (3 < col < 10) or (1 < row < 6) and (3 < col < 7)):
        return 'Z'
    elif ((3 < row < 6) and (3 < col < 10)):
        return 'X'
    elif (((10 <= col < 13) or (6 < col < 10)) and (3 < row < 7)):
        return 'B'
    else:
        return 'T'

if __name__ == '__main__':
        driver.comparePatterns(letter)
