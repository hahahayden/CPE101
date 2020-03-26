# Name: Giselle Dougan, Hayden Tam
# Teacher: S. Einikan
# CPE101
# Section: 05
import sys
from puzzle import*
from fade import*
from blur import*


def main():
    args = sys.argv

    if (len(args) == 2):           # if length of argument is 2 then run puzzle function

        argu2 = args[1]
        try:

            fin = open(argu2, "r")
            puzzleMain(fin)
        except:
            if(args[1]). isnumeric() == False:
                # if it can't open the file; usage error
                print("Unable to open " + args[1])
                exit()
            elif(args[1].isnumeric() == True):
                print("Puzzle(decoding) Usage-  python pixelImage.py image_file.ppm")
                exit()

            # if length is 5 use fade function
    elif (len(args) == 5):
        try:
            if(type(int(args[2])) == int and type(int(args[3])) == int and type(int(args[4])) == int):
                fin = open(args[1], "r")
                fadeMain(fin, args[2], args[3], args[4])

        except IOError:                                     # if it can't open the file; usage error
            print("Unable to open " + args[1])
            exit()
        except:
            print("Fade Usage- python pixelImage.py <image> <row> <column> <radius>")
            exit()

    # if length is 3 use blur function
    elif (len(args) == 3):
        try:
            if(type(int(args[2])) == int):

                fin = open(args[1], "r")
            # takes in the file and the arguments
                blurMain(fin, args)

        except IOError:  # if it can't open the file; usage error
            print("Unable to open " + args[1])
            exit()
        except:
            print("Blur Usage- python pixelImage.py <image> <reach>")
            exit()

    else:
        print("Usage Error: Please check your command line")
        print("Puzzle(decoding) Usage-  python pixelImage.py image_file.ppm")
        print("Fade Usage- python pixelImage.py <image> <row> <column> <radius>")
        print("Blur Usage- python pixelImage.py <image> <reach>")
        exit()


if __name__ == "__main__":
    main()
