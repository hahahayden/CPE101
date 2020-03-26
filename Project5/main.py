import sys
from puzzle import*
from fade import *

args=sys.argv
try:
    if (args[0]=="puzzle.py"):
        
        fin=open(args[1],"r")
        puzzleMain(fin)
   
    else:
        print("Unable to open "+args[1])
except:
    exit()

    