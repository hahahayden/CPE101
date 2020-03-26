#Project3- Tic-Tac-Toe Simulator
#Name: Hayden Tam
#Instructor: S. Einakian
# Section: 05

import random
#Purpose: to welcome the user and to take an input for number of players
#Signature: None-> int
def Welcome():
    x=1
    print("Welcome to this Tic-Tac-Toe Simulator")
    print("Your goal is to line up 3 of your tics in either a line or a diagonal.")
    print("You will pick either X or O. X will go first")
    while(x==1):
        
        players=int(input("Do you wish to play against a (1)computer, or with (2)Players?"))
        print()
        if(1<=players<=2):
            x+1
            return players
        else:
            x=1
            print("Please enter 1 or 2:")

# Purpose: creates a board that shows the designated places 
# Signature: None->list
def createBoard():
       
    list=[" ", " ", " ", " ", " ", " ", " ", " ", " "] 
    count=0
    num=1
    print()
    print("The board positions are as follows:")
    for spaces in list:
        
        if((count+1)%3 !=0 and count<9):
            print("",num, end="  |")
            count+=1
            num+=1
            
        elif ((count+1) %3==0 and count<8):
        
            print(" ", num)
            print()
            print("---------------")
            count+=1
            num+=1
        else:
            print(" ", num)
  
    return list                                        # returns a blank list

#Purpose: prints the board with updated values
#Signature: list->none

def printBoard(mainList):
   
    count=0                                                

    for spaces in mainList:
        
        if((count+1)%3 !=0 and count<9):
            print(" ",mainList[count],end=" |")
            count+=1
            
        elif ((count+1) %3==0 and count<8):
        
            print(" ", mainList[count])
            print()
            print("---------------")
            count+=1
            
        else:
            print(" ", mainList[count])
    

#Purpose: picks a letter (X or O)
#Signature: none-> string

def pickLetter():
  
    x=1
    while(x==1):  
        letter=input("Choose X or O:") 
        if(letter=="X" or letter=="O"):
          
           x+=1
           return letter
        else:
            print("Please pick X or O! Not that HARD!")

#Purpose: Asks for location to place the letter
#Signature: string, list->list
def getInput(letter, mainList):
    x=0    
    while(x==0):
        position=int(input("Where do you like to place your letter (pick in range of 1-9):"))
        
       
        if (position <1 or  position> 9):                                   # if position isn't within range it reprompts
            print("Please enter a number between 0 and 9 por favor!")
        elif(mainList[position-1]==("X") or mainList[position-1]==("O")):
            print("Invalid move! Location is already taken. Please try again.")
            print()
        else:
            mainList[position-1]=letter
            x+=1
            return mainList   

#Purpose: Checks each row for same letters
#Signature: list-> boolean, string
def checkRows(gameBoard):

    for count in range(0,8,3):
        if(gameBoard[count]==gameBoard[count+1]==gameBoard[count+2]!= " "):
            
            return True, gameBoard[count]
        
    return False, " "
#Purposes: Checks each column for same letters
#Signature: list->boolean
    
def checkCol(gameBoard):
    
    for count in range(0,3,1):
        if(gameBoard[count]==gameBoard[count+3]==gameBoard[count+6]!=" "):
            return True, gameBoard[count]
      
    return False, " "
#Purpose: Checks the diagonals for same letters
#Signature: list->boolean, string
def checkDiag(gameBoard):
    if ((gameBoard[0]  == gameBoard[4]  == gameBoard[8]!=" ")):
        return True, gameBoard[0]
   

    elif ((gameBoard[2]  == gameBoard[4]  ==gameBoard[6] !=" " )):
        return True, gameBoard[2]                          # diagonal returns the letter that it equals                       

    return False, " "
    
#Purpose: Checks if the entire board is full
#Signature: list->boolean,string
def boardFull(gameBoard):
     for i in range(0, 9):
        
        if (gameBoard[i]==" "):  
            return False
        

     return True

#Purpose: Checks if anyone won
#Signature: list->boolean
def checkWin(gameBoard):
    
    if ((checkRows(gameBoard)[0] or checkCol(gameBoard)[0] or checkDiag(gameBoard)[0])==True):             #takes the letter from checkRows, checkCols, checkDiags to display winner
        print("Winner winner chicken dinner!")
        
        if(checkRows(gameBoard)[0]):
           print("Player with letter %s"%checkRows(gameBoard)[1], "wins!") 
           return True
        elif (checkCol(gameBoard)[0]):
           print("Player with letter %s"%checkCol(gameBoard)[1], "wins!")
           return True
        elif (checkDiag(gameBoard)[0]):
           print("Player with letter %s"%checkDiag(gameBoard)[1], "wins!")
           return True
        
    else:
        print("Board is full!")
        return False

#Purpose: Creates a random generator for the computer version of the game 
#Signature: string, list-> list
def inputComputer(letter,mainList): 
    x=0    
    while(x==0):
        computerNum=random.randint(1,9)
        
        if(mainList[computerNum-1]==("X") or mainList[computerNum-1]==("O")):
            continue
        else:
            mainList[computerNum-1]=letter
            x+=1
            return mainList   

#Purpose: Checks which player is playing currently  and displays the letter and player
#Signature: string, int, int->int

def turnCount(letter,player,count):
     
    print("It's Player  ", player,"'s(", letter, "'s) Turn" )
    count+=1
    return count

#Purpose: run two player mode 
#None->None
def runTwoPlayer():
    print()
    gameBoard=createBoard()
    print()
   
    letter=pickLetter()
    count=0   
    player=1
    
    print("Here is the board to use!")
   
    printBoard(gameBoard)
    
    while(boardFull(gameBoard)==False):                   #assigns player 2 to X if O is selected; if not Player 1 is X
        print()
        if (count==0 and count%2==0 and letter=="O"):
            letter="X"
            player=2
        elif (count==0 and count%2==0 and letter=="X"):
           
            letter="X"
            player=1

        count=turnCount(letter,player,count)
        gameBoard=getInput(letter,gameBoard)

        if (count%2!=0 and letter=="X" and player==1):              #switches players depending on what turn and who went 
                                                                    #if player 1 is X and odd count it gets input switching the letter to O and 2
            letter="O"
            player=2

        elif (count%2==0 and letter=="O" and player==2):           #if player 1 is O and even count it gets input switching the letter to X and 1
           
            
            letter="X"
            player=1
        
        elif(count%2!=0 and letter=="X" and player==2):           #if player 2 is X and odd count it gets input switching the letter to O and 1
            
           
            letter="O"
            player=1
       
        
        elif (count%2==0 and letter=="O" and player==1):          #if player 1 is O and even count it gets input switching the letter to X and 2
            
            
            letter="X"
            player=2
          
        print()
    
        printBoard(gameBoard)
        
        result=checkRows(gameBoard)
        result2=checkCol(gameBoard)

        result3=checkDiag(gameBoard)
        resultBool=result[0]
        result2Bool=result2[0]
        result3Bool=result3[0]
        if(resultBool==True or result2Bool==True or result3Bool==True):    #breaks out the while loop if a tictactoe is found
              
            break
        
        
        
        playerWinner=player

    if( checkWin(gameBoard)):
       print("Good job Player", playerWinner, "for winning!")
    else:
       print("No one wins!")

        
#Purpose: run computer version(1) player
# Signature: None->None     
def runComputer():
    print()
    gameBoard=createBoard()
    print()
    
    letter=pickLetter()
    count=0  
    player=1
    print("Here is the board to use!")
    print()
    printBoard(gameBoard)
    print()
    while(boardFull(gameBoard)==False):       #assigns player X to 2 if O is selected; if not X is player 1
        print()
        if (count==0 and count%2==0 and letter=="O"):
            letter="X"
            player=2
        elif (count==0 and count%2==0 and letter=="X"):
            
            letter="X"
            player=1

        count=turnCount(letter,player,count)
       
       
        if (count%2!=0 and letter=="X" and player==1):      #if player 1 is X and odd count it gets input switching the letter to O and 2
            gameBoard=getInput(letter,gameBoard)
            
            
            letter="O"
            player=2

        elif (count%2==0 and letter=="O" and player==2):   #if player 2 is O and even count it gets input switching the letter to X and 1
            gameBoard=inputComputer(letter,gameBoard)
            
            letter="X"
            player=1
        
        elif(count%2!=0 and letter=="X" and player==2):     #if player 2 is X and odd count it gets input switching the letter to O and 1
            
            gameBoard=inputComputer(letter,gameBoard)          
            letter="O"
            player=1
       
        
        elif (count%2==0 and letter=="O" and player==1):     #If O is chosen first; player 2 becomes O and player 1 is X(computer generator is player 1)
            
            gameBoard=getInput(letter,gameBoard)
            letter="X"
            player=2
          
      
            
        print()
        printBoard(gameBoard)
        result=checkRows(gameBoard)
        result2=checkCol(gameBoard)

        result3=checkDiag(gameBoard)
        resultBool=result[0]
        result2Bool=result2[0]
        result3Bool=result3[0]
        
        if(resultBool==True or result2Bool==True or result3Bool==True):
            
            break
        
        
        
        playerWinner=player

    if( checkWin(gameBoard)):
       print("Good job Player", playerWinner, "for winning!")
    else:
       print("No one wins!")