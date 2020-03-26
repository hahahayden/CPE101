# Name: Hayden Tam
# Teacher: S. Einikan
# CPE-101
# Section: 05

import sys

# Purpose: checks if the input is an integer
# Signature: list-> bool


def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Purpose: checks if the input is a float
# Signature: list-> bool


def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def main():

    if(len(sys.argv) >= 2):  # makes sure the arguments necessary are given; if not print usage
        args = sys.argv

    else:
        print("[-s] file_name")
        exit()
    # if -s isn't given and the length is bigger than expected print usage
    if("-s" not in args and len(sys.argv) == 3):
        print("[-s] file_name")
        exit()
    try:
        # than try to locate the file and if it can't open; print what is there that can't be opened
        number = args.index("test0.txt")
        fin = open(args[number])
    except:
        if(len(sys.argv) == 2):
            print("Unable to open", args[1])

        exit()

    try:
        # open the file since all the excpetions have passed
        fin = open(args[args.index("test0.txt")])

        integerCount = 0
        floatCount = 0
        otherCount = 0
        total = 0

        for count in fin:

            newFin = count.strip().split()

            for count2 in range(len(newFin)):

                if RepresentsInt(newFin[count2]) == True:
                    total += (int(newFin[count2]))
                    integerCount += 1

                elif RepresentsFloat(newFin[count2]) == True:
                    total += (float(newFin[count2]))
                    floatCount += 1
                else:
                    otherCount += 1

        print("Integer:", integerCount)
        print("Float:", floatCount)
        print("Other:", otherCount)
        if "-s" in args:  # if -s is shown in the command line print the sum
            print("Sum:", total)
    except:

        print("Unable to to open", fin)
        exit()


if __name__ == '__main__':
    main()
