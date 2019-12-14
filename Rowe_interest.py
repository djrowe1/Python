#David Rowe
#COP2002.001
#11-29-2019 ver1
#Project 6 - Loan Interest Calculator

#variables
#str(loan)      user input for loan amount
#str(rate)      user input for interest rate
#str(cost)      calculated value for amount of interest for loan

    #To do
    #prompt user for loan amount and interest rate
    #convert loan and rate to valid decimal format and then calculate interest
    #display loan information with loan, rate, and cost
    #ask user if another interest calculation is needed

from decimal import Decimal
from decimal import ROUND_HALF_UP
import locale as lc

def main():                         #call functions within control loop
    calc = 'y'
    print ("Welcome to the Interest Calculator")
    while (calc == 'y' or calc == 'Y'):
        loan, rate = getLoan()
        cost = calculate(loan, rate)
        displayPlan (loan, rate, cost)
        calc = newCalc()
    print("")
    print("Goodbye!!!")
            
def getLoan():                      #get user input for loan information and convert string as needed
    print ("")
    loan = input("Please enter loan amount: ")
    print ("")
    rate = input("Please enter interest rate: ")
    print ("")
    #convert user input as needed to clean-up strings before converting to Decimal
    if loan.isdigit():
        loan = Decimal(loan)
    else:
        loan = loan.replace("$", "")
        loan = loan.replace(",", "")
        k = loan.find("k")
        if k != -1:
            loan = loan.replace("k", "")
            loan = (Decimal(loan))*1000
        loan = Decimal(loan)
    if rate.isdigit():
        rate = (Decimal(rate))/100
    else:
        rate = rate.replace("%", "")
        rate = (Decimal(rate))/100
    return loan, rate
    
def calculate(loan, rate):           #calculate cost of loan
    cost = Decimal(loan*rate)
    cost = cost.quantize(Decimal("1.00"), ROUND_HALF_UP)
    return cost

def displayPlan(loan, rate, cost):   #display loan cost with interest
    result = lc.setlocale(lc.LC_ALL, "")
    if result == "C":
        lc.setlocale(lc.LC_ALL, "en_US")
    print("{:20} {:>16}".format("Loan Amount:", lc.currency(loan, grouping=True)))
    print("{:20} {:>16.3%}".format("Interest Rate:", (rate)))
    print("{:20} {:>16}".format("Interest Amount:", lc.currency(cost, grouping=True)))
    print("")
    return

def newCalc():                       #prompt user for another loan calculation
    print("")
    calc = input("Continue with new calculation? (y/n): ")
    return calc
   
if __name__ == "__main__":           #if started as the main module, call the main function
    main()
