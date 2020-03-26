# Name: Giselle Dougan, Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05

import sys

# Purpose: groups the list into sublists of threes
# Signature: list-> list


def group3(listVal):
    newL = []

    for count2 in range(len(listVal)):
        if count2 % 3 == 0:
            newL.append(listVal[count2:count2+3])

    return newL

# Purpose: takes in the txt file and splits it into a list, groups it and then decodes the image
# Signature: string-> None


def puzzleMain(fin):

    newList = []
    for count in fin:
        newFin = count.strip()
        newList.append(newFin)

    newList2 = newList[3:]

    group3List = group3(newList2)

    fin2 = open("hidden.ppm", "w")
    fin2.write(str("P3")+"\n")
    fin2.write(newList[1]+"\n")
    fin2.write(newList[2]+"\n")
    for countList in range(len(group3List)):

        if(int(group3List[countList][0]) < 255):
            newResult = int(group3List[countList][0])*10

        elif(int(group3List[countList][0])*10) > 255:
            newResult = 255
        fin2.write(str(newResult))
        fin2.write("\n")
        fin2.write(str(newResult))
        fin2.write("\n")
        fin2.write(str(newResult))
        fin2.write("\n")

    fin2.close()
    fin.close()
