#Signature: string-> string
#Purpose: rotates 13 position for all position of string input
def str_rot_13 (string):
    string2=""
    for count in range(len(string)):
        newchar=ord(string[count])+13
        if(string[count].islower and newchar>122):
            newchar=newchar-ord("z")+ord("a")-1
        
   

        elif(string[count].isupper and 90<newchar<96):
            newchar=newchar-ord("Z")+ord("A")-1
        letter=chr(newchar)
        string2+=letter
    return string2
#Signature: string, string, string->string
#Purpose: uses a given string and replaces letters to be found with given ones

def str_translate_101(string,charFind,charSwitch):
    
    list1=[charSwitch if i ==charFind else i for i in string]
    newString="".join(list1)
    return newString




