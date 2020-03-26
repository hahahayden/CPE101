# Project 2 - Moonlander
#
# Name: Hayden Tam
# Instructor: S. Einakian
# Section: 05


#Display welcome message
#None->None

def showWelcome():
    print()
    print("Welcome aboard the Lunar Module Flight Simulator")
    print()
    print("   "+"To begin you must specify the LM's initial altitude")
    print("   "+"and fuel level.  To simulate the actual LM use")
    print("   "+"values of 1300 meters and 500 liters, respectively.")
    print()
    print("   "+"Good luck and may the force be with you!")
    print()

#Get input for Fuel
#None->int

def getFuel():
    y=0
    while y==0:

        value=int(input("Enter the initial amount of fuel on board the LM (in liters): "))
        
        if (value<=0):
            y=0
            print("ERROR: Amount of fuel must be positive, please try again")
            
        elif (value>0):
            y+=1
            break
    return value

#Get input for the Altitude
#None->int

def getAltitude():
    x=0
    while(x==0):
        altitude=float(input("Enter the initial altitude of the LM (in meters): "))
        if (1<=altitude<=9999):
            x+1
            return altitude
        else:
            print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
            
#Display Lunar Module State
#int,float, float, int, int-> none
    
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    elapsedTime=int(elapsedTime)
    
    velocity=float(velocity)
    velocity=round(velocity,2)
    fuelAmount=int(fuelAmount)
    fuelRate=int(fuelRate)
    altitude=round(altitude,2)
 
    x="Elapsed Time:"
    y="Rate:"
    z="Fuel:"
    a=" Altitude:"
    print("%13s %4d %s"%(x,elapsedTime,"s") )    #%5d
    
    print("%13s %4d %s"% (z,fuelAmount,"l"))
    print("%13s %4d %s"%(y,fuelRate,"l/s"))
    
    print("%13s %7.2f %s"% (a,altitude,"m"))
    print("%13s %7.2f %s"% ("Velocity:",velocity,"m/s"))

#Get user to input Fuel Rate
#int->int 

def getFuelRate(currentFuel):
    x=0
    while(x==0):
        fuelRate=int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
               
        if(0<=fuelRate<=9 and fuelRate<=currentFuel):

            return fuelRate

        elif(0<=fuelRate<=9 and fuelRate>currentFuel):
            
            return currentFuel
       
        elif(fuelRate<0 or fuelRate>9):
            print("ERROR: Fuel rate must be between 0 and 9, inclusive")
            print()

#Display the landing status of the Lunar Module
#float(double)->none

def displayLMLandingStatus(velocity):
    if (-1<=velocity<=0):
        print("Status at landing - The eagle has landed!")
    elif (-10<velocity<-1):
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif (velocity<=-10):
        print("Status at landing - Ouch - that hurt!")

#Display the Out of Fuel Statements after Fuel is out
#int, float(double), float(double), int, int-> none

def displayLMStateOutofFuel(elapsedTime,altitude,velocity,fuelAmount,fuelRate):
    elapsedTime=int(elapsedTime)

   
    print("OUT OF FUEL - Elapsed Time:","%3d"%(elapsedTime),"Altitude:","%7.2f"%(altitude),"Velocity:", "%7.2f"%(velocity))




#Functions that Calculate

#Calculate your updated acceleration
#float, int-> float

def updateAcceleration(gravity,fuelRate):

    gravity=float(gravity)
    fuelRate=int(fuelRate)
    accelTP1=gravity*((fuelRate/5)-1)
    return accelTP1

#Calculations to update altitude
#float, float,float->float
def updateAltitude(altitude,velocity,acceleration):
    
    altitudeTP1=altitude+velocity+(acceleration/2) #acceleration from updated
    return altitudeTP1

#Calculate your updated velocity
#float, float-> float
def updateVelocity(velocity,acceleration):
    velocityTP1=velocity+acceleration         #acceleration from updated
    return velocityTP1

#Calculate updated fuel
#int,int->int

def updateFuel(fuel,fuelRate):
    fuelTP1=fuel-fuelRate
    return fuelTP1



