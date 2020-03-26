#Signature:string->boolean
#Purpose: determines if character input is lower case
def is_lower_101(char):
    
    if(ord(char)> ord("a")-1):
        return True
    else:
        return False

#Signature: string-> string
#Purpose: add 13 to the letter  so a becomes n and so on
def char_rot13(char):
    newchar=ord(char)+13
    
    if(char.islower and newchar>122):   #change ord
        newchar=newchar-ord("z")+ord("a")-1
        
   

    elif(char.isupper and 90<newchar<96):
        newchar=newchar-ord("Z")+ord("A")-1

    return chr(newchar)
    



