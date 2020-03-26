# Program 4
#
# Name: Hayden Tam, Sid Sharma
# Instructor: S. Einakian
# Section: 05

# Purpose: take in an input for 100 character string
# Signature: None-> String


def userInput():
   
    
    string=input()    
    return string

# Purpose: print the list in 10x10 matrix form
# Signature: string-> None


def printMatrix(list):
    print("Puzzle:")
    print()

    for count in range(len(list)):
        if((count % 10 != 0 or count == 0)):
            print(list[count], end="")
        else:
            print() 
            print(list[count], end="")
    print()

#Purpose: get user input for the words needed to be found
#Signature: none-> string

def userWord():
    
    user=input()
    return user

# Purpose:Flip the String back to front
# Signature: string->string


def flipString(userString):
    
    reverseString = userString[::-1]    # Flip the string from back to front

    return reverseString
    


# Purpose:Flip string column to row
# Signature: string,integer-> string


def transpose_string(string, row_len):                         #transpose string method makes the strings into columns 

    
    
    start = 0
    trans_string = ""
    for row in range(start, row_len):
        for column in range(row, 100, row_len):                  # FLIPS ONLY A 100; doesn't reach the \r stuff
            
            trans_string+=string[column]                        #concatenates the string

    return trans_string



# Purpose: check Forward for the words
# Signature: string, string-> boolean


def checkForward(userString, split_words):                  
    puzzle = []
    string_result = ""                                      # First, split the 100 character string into 10 strings in a list
    for i in range(10):
        puzzle.append(userString[10*i:(10*i)+10])           # 10 per item in the list so it keeps track of one line only
        
    for string in range(len(puzzle)):                       #string is basically my row; puzzle[0] returns row 0 
        
        if(puzzle[string].find(split_words)) > -1:
            index = puzzle[string].find(split_words)         # finds where it is in the row; the column
            string_result = "{0}: {1} row: {2} column: {3}".format(
                split_words, '(FORWARD)', string,index)
            return string_result
    return None

# Purpose: check backwards for the word
# Signature: string,string->boolean

def checkBackward(userString, findWordList):                 
    reverseUserString = flipString(findWordList)            #Flips the word list so it can find the word in reverse form in the 100 character string
    puzzle = []      
    
    string_result = ""
    for i in range(10):                                     # create a list of the 100 characters with 10 strings in the list
        puzzle.append(userString[10*i:(10*i)+10])
        
    for string in range(len(puzzle)):                       #string is my row 
        
        if(puzzle[string].find(reverseUserString)) > -1:
            index = puzzle[string].find(reverseUserString)            #index is the column but since it is reverse we have to add the length of the string-1 to get actual position
            string_result = "{0}: {1} row: {2} column: {3}".format(
                findWordList, '(BACKWARD)', string,index+len(reverseUserString)-1)
            return string_result
        
    return None





# Purpose: check down for the word
# Signature: string, string-> boolean


def checkDown(userString, findWordList):

    transposed = transpose_string(userString, 10)  # transpose string
    
    puzzle = []
    string_result = ""
    for i in range(10):
        puzzle.append(transposed[10*i:(10*i)+10])                  #makes a list of 10 strings
        
    for string in range(len(puzzle)):  # row
        
        if(puzzle[string].find(findWordList)) > -1:                           #basically the reverse so string is the row and columns is string
            index = puzzle[string].find(findWordList)
            string_result = "{0}: {1} row: {2} column: {3}".format(
                findWordList, '(DOWN)', index, string)
            return string_result
    return None


# Purpose: check upwards for the word
# Signature: string, string-> boolean


def checkUp(string, findWordList):                                   
    trans_string = transpose_string(string, 10)              #Tranposes the strng and flips the string to make the string display the wanted word in the right away
    
    flipWordList = flipString(trans_string)
    
    puzzle = []
    string_result = ""
    for i in range(10):
        puzzle.append(flipWordList[10*i:(10*i)+10])
        
    for string in range(len(puzzle)):
        if puzzle[string].find(findWordList) > -1:                      #row is still the index; but since it is reversed for row you have to minus by the final index(9)
            index = 9-puzzle[string].find(findWordList)
            string_result = "{0}: {1} row: {2} column: {3}".format(
                findWordList, '(UP)', index, 9-string)
            return (string_result)
    
    return None