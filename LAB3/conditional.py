# Lab 3
#
# Name:Hayden Tam 
# Instructor: Sussan Einakian
# Section: 05

#To tell the greater of two numbers
#int int -> int
def max_101(x,y):
   if (x>y):
      return(x)
   else:
      return(y)

#To determine max out of three numbers

#float,float,float->float
def max_of_three(x,y,z):
   if (x>y and x>z):
      return x
   elif (y>x and y>z):
      return y
   else:
      return z
 
#Return fee after a certain amount of hours
#Int->Float 
def rental_late_fee(x):
   if (x<=0):
      fee=0
      return fee
   elif (0<x<=9):
      fee=5
      return fee
   elif (9<x<=15):
      fee=7
      return fee
   elif (15<x<=24):
      fee=19
      return fee
   else:
      fee=100
      return (fee)
