#David Rowe
#COP2000.001
#11-05-2019 ver1
#Project 3 - Real Estate Values working with list items

def main():
    #list & variables
    #priceList = []         #list that holds home values
    #int(average)           #stores average from list
    #int(median)            #stores median from list
    #int(minimum)           #stores minimum home price in list
    #int(maximum)           #stores maximum home price in list
 
    priceList = []          #list for holding home values
    
    setPrices(priceList)                                         #function for adding home values to list
    average, minimum, maximum, median = getStats(priceList)      #function for calculating required statistics
    displayStats (priceList, average, minimum, maximum, median)  #function to display stats for home values

def setPrices(priceList):
    #adds home values to list
    
    print ("Real Estate Values")
    print ("")
    print ("***************************************************")
    price = 0                                                    #local variable for adding to list 
    while (price != -99):
        price = float(input("Please enter cost of one home or -99 to quit: "))
        if (price != -99):
            priceList.append(price)
    priceList.sort()                                             #sorts home values in ascending order

def getStats(priceList):
    #calculates statistical information for home values
    
    import math                                                  #makes math module available
    total = 0                                                    #local variable for summing home values
    first = 0                                                    #local variable for calculation in (even) median value
    second = 0                                                   #local variable for calculation in (even) median value
    middle = 0                                                   #local variable for calculation in (odd) median value
    
    #finds the average home value in the list
    for home in priceList:
        total = total + home
    average = total / len(priceList)

    #finds minimum and maximum home values in list
    minimum = min(priceList)
    maximum = max(priceList)

    #finds the median home value in the list
    if (len(priceList) % 2 == 0):                                #selects when the list is even
        first = int((len(priceList))/2)
        second = int(((len(priceList))/2)-1)
        median = (priceList[first] + priceList[second])/2
    elif (len(priceList) % 2 == 1):                              #selects when the list is odd
        middle = int(math.ceil((len(priceList))/2)-1)
        median = priceList[middle]
    return average, minimum, maximum, median                     #Oh my... only in Python!!!

def displayStats(priceList, average, minimum, maximum, median):
    #displays statistical information for home values
    
    print ("***************************************************")
    print ("Prices of homes in your area:")
    print (priceList)
    print ("***************************************************")
    print ("The median value is $" + str(median))
    print ("The average sale price is $" + str(average))
    print ("The minimum sale price is $" + str(minimum))
    print ("The maximum sale price is $" + str(maximum))
    
main()
