# Project1
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section:05

import math

#Purpose:To convert weight from pounds to kilograms
#Signature:float->float

def poundsToKG(pounds):
   weightkg=pounds*.453592
   return weightkg

#Purpose: To take in the object user wants to throw and output the weight of that certain object
#Signature: string->float
    
def getMassObject(object):
   if object=='t':
       weightObj=.1
   elif object=='p':
       weightObj=1.0
   elif object=='r':
       weightObj=3.0
   elif object=='g':
       weightObj=5.3
   elif object=='l':
       weightObj=9.07
   else:
       weightObj=0.00
   return weightObj

#Purpose: calculate the velocity of the object being thrown
#Signature: float->float

def getVelocityObject(distance):
   gravity=9.8
   velocityObject=math.sqrt((gravity*distance)/2)
   
   return velocityObject

#Purpose: calculate the velocity of the skater
#Signature: float,float,float->float

def getVelocitySkater(massSkater,massObject,velObject):
   velocitySkater= (massObject*velObject)/massSkater
   velocitySkater=round(velocitySkater,3)
   return velocitySkater


