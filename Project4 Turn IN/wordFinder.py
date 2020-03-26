# Program 4
#
# Name: Hayden Tam, Sid Sharma
# Instructor: S. Einakian
# Section: 05
from funcs import *

def main():
  
    string=userInput()                                         #get characters for puzzle
    
    words=userWord()                                           #get words to find
    
   
    printMatrix(string)
    
    
    
    

    split_words=words.split()                                   #split the find words by spaces
    
    for word in split_words:                                    # go through each word in split words and find the word from the 10 character strings
        if checkForward(string,word)!=None:
            print(checkForward(string, word))
        elif checkBackward(string,word)!=None:
            print(checkBackward(string,word))
    
    
        elif checkDown(string,word)!=None:
            print(checkDown(string, word))
        elif checkUp(string,word)!=None:
            print(checkUp(string,word))
        else:
            stringNotFound="{0}: word not found".format(
            (word))
            print(stringNotFound)
    
if __name__=="__main__":
   main()