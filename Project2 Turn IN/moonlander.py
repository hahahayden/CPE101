# Project 2 - Moonlander
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05


import landerFuncs

def main():
    
    gravity=1.62
    velocity=0.00
    fuelRate=0
    landerFuncs.showWelcome()
    altitude=landerFuncs.getAltitude()
    fuel=landerFuncs.getFuel()
    elapsedTime=0
   
    print()
    print("LM state at retrorocket cutoff")
    landerFuncs.displayLMState(elapsedTime,altitude,velocity,fuel,0)
    print()
    
 
    while(fuel>0 and altitude>0):          #while fuel>0 and altitude>0 display message vertically
   
        
        fuelRate=landerFuncs.getFuelRate(fuel)
        updatedAcceleration=landerFuncs.updateAcceleration(gravity,fuelRate)

        
        elapsedTime+=1                #add time by one to count
        updatedVelocity= landerFuncs.updateVelocity(velocity,updatedAcceleration)      #calculate velocity, from the updated acceleration
        updatedAltitude=landerFuncs.updateAltitude(altitude,velocity,updatedAcceleration)  #update altitude
        updatedFuel= landerFuncs.updateFuel(fuel,fuelRate)
        fuel=updatedFuel                          #set updated variables back to parameter variables
        velocity=updatedVelocity
        altitude=updatedAltitude

        if(fuel>0 and altitude>0):     #only display if true, if not break out of the while

            landerFuncs.displayLMState(elapsedTime,updatedAltitude,updatedVelocity,fuel,fuelRate)  
            print()

        elif(altitude<=0):
            break

    while(altitude>0 and fuel==0):    #while true display vertically out of fuel statement 
        
        landerFuncs.displayLMStateOutofFuel(elapsedTime,updatedAltitude,updatedVelocity,0,fuelRate)

        fuelRate=0
        elapsedTime+=1
        updatedAcceleration=landerFuncs.updateAcceleration(gravity,fuelRate)
        updatedVelocity= landerFuncs.updateVelocity(velocity,updatedAcceleration)
        updatedAltitude=landerFuncs.updateAltitude(altitude,velocity,updatedAcceleration)
        updatedFuel= landerFuncs.updateFuel(fuel,fuelRate)
        
       
             
        velocity=updatedVelocity
        altitude=updatedAltitude
    if (altitude<=0):                #once altitude reaches zero display altitu$
        updatedAltitude=0
   
    
    print()
    print("LM state at landing/impact")
    landerFuncs.displayLMState(elapsedTime,updatedAltitude,updatedVelocity,fuel, fuelRate)     
    print()  
    landerFuncs.displayLMLandingStatus(updatedVelocity)
        
  

    
    
if __name__=="__main__":
   main()

