# Project1
#
# Name: Hayden Tam
# Instructor: S.Einakian
# Section:05

import math
import funcs
def main():
   pounds=float(input("How much do you weigh (pounds)? "))
   distance=float(input("How far away your profesor is (meters)? "))
   object=(input("Will you throw a rotten (t)omato,banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? "))
   massObject=funcs.getMassObject(object)                                  # Get the mass of the object
   massSkater=funcs.poundsToKG(pounds)                                     # Convert pounds to kg for skater
   velObj=funcs.getVelocityObject(distance)                                # Get velocity of obj
   velocitySkater=funcs.getVelocitySkater(massSkater,massObject,velObj)    # Get velocity of obj   
   
  # Display comment based on the mass of thrown obj and distance thrown

   if (massObject<=.1):
       print("Nice throw! You're going to get an F!")
   elif((massObject>.1) and (massObject<=1.0)):
       print("Nice throw! Make sure your professor is OK.")
   elif (massObject>1.0):
       if (distance<20):
           print("Nice throw! How far away is the hospital?")
       elif (distance>=20):
           print("Nice throw! RIP professor.")
   
  # Print velcoity of skater 
   print("Velocity of Skater:",velocitySkater,"m/s") 
  
   
# Display comment based on velocity
   if (velocitySkater<.2):
       print("My grandmother skate faster than you!")
   elif (velocitySkater>=.2)and (velocitySkater<1.0):
       pass
   elif (velocitySkater>=1.0):
       print("Look out for that railing!!!")
     
if __name__=="__main__":
   main()

