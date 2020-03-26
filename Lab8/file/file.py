# LAB8
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05

import sys
args = sys.argv
fin = open("in.txt", "r")

count = 0
fin2 = fin.readlines()

# Takes the rows minus the last one and strips it by \n goes through each and counts the characters and prints the line
for row in range(len(fin2)-1):

    row = fin2[row].strip("\n")

    length = (len(row))

    print("Line ", count, "(", length, "chars): ", row)
    count += 1
