#David Rowe
#COP2002.001
#11-22-2019 ver1
#Project 5 - Aircraft Fuel Calculator

#variables
#str(plan)      loop control variable
#int(miles)     user input for flight miles
#float(time)    used to calculate flight time based on miles
#int(hours)     used to store hours of flight time
#int(minutes)   used to store minutes of flight time
#float(fuel)    used to store gallons of fuel for flight

    #To do
    #prompt user for flight plan in nautical miles
    #calculate and convert miles to time then calculate time to gallons
    #display flight plan calculations
    #ask user if another flight plan calc. is needed

import math

def main():                 #call functions within control loop
    plan = 'y'
    print ("Aircraft Fuel calculator")
    while (plan == 'y' or plan == 'Y'):
        miles = getMiles()
        hours, minutes, fuel = calculate(miles)
        displayPlan (miles, hours, minutes, fuel)
        plan = newPlan()
    print("")
    print("Goodbye and Safe travels!!!")
            
def getMiles():             #get user input for flight miles
    print ("")
    miles = int(input("Please enter distance in nautical miles: "))
    print ("")
    print ("***********************************************")
    print ("")
    return miles
    
def calculate(miles):       #calculate time in hours and minutes based on distance and calculate gallons of fuel needed based on time
    time = miles/120
    hours = math.floor(time)
    minutes = int((time*60) % 60) 
    fuel = round(8.4*(time+.5), 1)  #added .5 hour to flight time for fuel calcualtions
    return hours, minutes, fuel

def displayPlan(miles, hours, minutes, fuel):   #display flight plan calculations
    print("Planned travel distance in nautical miles: " + str(miles))
    print("Fight time will be: " + str(hours) + " hour(s) and " + str(minutes) + " minute(s)")
    print("Required fuel for flight: " + str(fuel) + " gallons")
    return

def newPlan():              #prompt user for another flight plan calculation
    print("")
    plan = input("Continue with another flight plan? (y/n): ")
    return plan
   
if __name__ == "__main__":  #if started as the main module, call the main function
    main()
