#Lab 2 Functions
#Name: Hayden Tam
#Section: 05

import math

#Purpose: Calculate a cube of one number and a cube of another divided 
#by 5x+7
#Signature: int int ->float

def math_func1(x,y):
    numerator1=x**3
    numerator2=y**3
    numeratorTot=numerator1+numerator2
    denominator=5*x+7
    return numeratorTot/denominator

#Purpose: calculate the quadratc formula
#Signature: int int int -> float

def math_func2(a,b,c):
   numerator2=math.sqrt((b**2)-(4*a*c))
   numerator1=-b
   denominator= 2*a
   return((numerator1+numerator2)/denominator)

# Purpose: To calculate  the Euclidean distance between two points
# Signature: int int int int -> float

def d(x1,y1,x2,y2):
   distance1=(x1-x2)**2
   distance2=(y1-y2)**2
   calculation=math.sqrt(distance1+distance2)
   return(calculation)

#Purpose: To check if a number is negative or not
#Signature: int->boolean

def is_negative(h):
   return (h<0)

#Purpose: To check if a number is divisble by 5
#Signature: int -> boolean

def dividable_by_5(num1):
   x=num1%5
   return (x==0)
