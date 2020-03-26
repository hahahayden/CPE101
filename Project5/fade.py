# Name: Giselle Dougan, Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05
import math
import sys

# Purpose: computes the distance between points
# Signature: int, int, int, int-> float


def computeDistance(currRow, currCol, specRow, specCol):
    inside = ((specCol-currCol)**2)+((specRow-currRow)**2)
    total = math.sqrt(inside)

    return total


# Purpose: groups the list into sublists of threes
# Signature: list-> list

def group3(listVal):
    newL = []
    for count2 in range(len(listVal)):
        if count2 % 3 == 0:
            newL.append(listVal[count2:count2+3])
    print(newL)
    return newL

# Purpose:Takes in the arguments given along with the strings within the text file and fades around the computed distance
# Signature: string,int,int,int-> None


def fadeMain(fin, arg2, arg3, arg4):

    # Length width bigger than 3

    newList = []
    for count in fin:
        newFin = count.strip()
        newList.append(newFin)

    newList2 = newList[3:]

    group3List = group3(newList2)

    fin2 = open("faded.ppm", "w")
    fin2.write(str("P3")+"\n")
    fin2.write(newList[1]+"\n")
    fin2.write(newList[2]+"\n")

    size = newList[1].split()               # split the sizes

    length = int(size[1])        # length width (dx)

    height = int(size[0])  # height

    for countList in range(len(group3List)):

        column = int(countList/length)  # gives the column of the picture
        row = int(countList % height)  # gives the row of the picture
        distance = int(computeDistance(
            row, column, int(arg2), int(arg3)))  # computes the distance
        radius = int(arg4)

        # subtracts the distance from the radius to get the faded outer part of circle
        multiplierNumerator = radius-distance
        multiplier = multiplierNumerator/radius

        if multiplier >= .20:

            newResult1 = int(int(group3List[countList][0])*((multiplier)))
            newResult2 = int(int(group3List[countList][1])*((multiplier)))
            # ultiple= max(.2, formula)
            newResult3 = int(int(group3List[countList][2])*((multiplier)))
            fin2.write(str(newResult1))
            fin2.write("\n")
            fin2.write(str(newResult2))
            fin2.write("\n")
            fin2.write(str(newResult3))
            fin2.write("\n")

        elif multiplier < .20:
            newResult1 = int(int(group3List[countList][0])*(.20))
            newResult2 = int(int(group3List[countList][1])*(.20))
            newResult3 = int(int(group3List[countList][2])*(.20))
            fin2.write(str(newResult1))
            fin2.write("\n")
            fin2.write(str(newResult2))
            fin2.write("\n")
            fin2.write(str(newResult3))
            fin2.write("\n")

    fin2.close()
