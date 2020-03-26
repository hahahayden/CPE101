
#Project3- Tic-Tac-Toe Simulator
#Name: Hayden Tam
#Instructor: S. Einakian
# Section: 05

from tictactoeFuncs import*

def main():
    
    numofPlayers=Welcome()
    if(numofPlayers==1):
        runComputer()
    elif(numofPlayers==2):
        runTwoPlayer()
            
    
if __name__=="__main__":
    main()

