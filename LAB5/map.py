#Name: Hayden Tam
# Instructor: S. Einakian
# Class: CPE 101-05
#Signature: list->list
#Purpose: Takes in a list and returns a list that only has positive integers
def are_positive(list):
    
    c=[]
    c=[list[x] for x in range(len(list))if (list[x]>0)]  #element that goes in the list is first
    return c
        

#signature: list, int->list
#Purpose: takes in a list and a number as a limit; only displays numbers greater than this number

def are_greater_than_n (list,n):
    c=[]
    
    for count in range(len(list)):
        
        if (list[count]>n):
           
            c.append(list[count])
            
    return c

#Purpose: If number in list is divisible by number, return the numbers in a list
#signature: list, int-> list
def are_divisible_by_n(list,n):
    c=[]
    count=0
    while count <len(list):
        if (list[count]%n==0):
            c.append(list[count])
        count+=1
    return c