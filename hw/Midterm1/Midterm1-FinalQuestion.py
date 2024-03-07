# Jack Estes
# 3/6/24
# IS303 Midterm 1
#
# Project that helps users build and sell cars for specific company and see the results of their labors.

# Vehicle class. Basic attributes for any type of vehicle
class Vehicle:
    def __init__(self, sMake="", sModel="", sColor=""):
        self.sMake = sMake
        self.sModel = sModel
        self.sColor = sColor


# Car class. Inherits from vehicle since there are other vehicles that aren't cars like trucks or boats.
class Car(Vehicle):
    def __init__(self, sMake="", sModel="", sColor="", sVIN="", sEngineDescription="", fTireSize=0.0, fBuildCost=0.0):
        super().__init__(sMake=sMake, sModel=sModel, sColor=sColor)
        self.sVIN = sVIN
        self.oEngine = Engine(sEngineDescription=sEngineDescription)
        self.listOfTires = [
            Tire(iPosition=0, fTireSize=fTireSize),
            Tire(iPosition=1, fTireSize=fTireSize),
            Tire(iPosition=2, fTireSize=fTireSize),
            Tire(iPosition=3, fTireSize=fTireSize),
        ]
        self.fBuildCost = fBuildCost


# Engine class
class Engine:
    def __init__(self, sEngineDescription=""):
        self.sEngineDescription = sEngineDescription


# Tire class
class Tire:
    # This helps to designate which tire position num correlates to the string that describes its position
    __tireMap = {
        0: "LF",
        1: "RF",
        2: "LR",
        3: "RR"
    }

    def __init__(self, iPosition=0, fTireSize=0.0):
        self.sTirePosition = self.__tireMap[iPosition]
        self.fTireSize = fTireSize


# Company class. Total company costs and revenues are private.
class Company:
    def __init__(self, sCompanyName="", fTotalCosts=0.0, fTotalEarnings=0.0):
        self.sCompanyName = sCompanyName
        self.__fTotalCosts = fTotalCosts
        self.__fTotalEarnings = fTotalEarnings

    def changeEarnings(self, fSalesEarnings=0.0):
        self.__fTotalEarnings += fSalesEarnings

    def changeCost(self, fBuildCosts=0.0):
        self.__fTotalCosts += fBuildCosts

    def getEarnings(self):
        return self.__fTotalEarnings

    def getCost(self):
        return self.__fTotalCosts


# Prints off info for each car stored in a list
def printCars(carsList):
    if carsList:
        print("REMAINING CARS:")
        for car in carsList:
            iPositionInList = carsList.index(car)
            sMake = car.sMake
            sModel = car.sModel
            sVin = car.sVIN
            sColor = car.sColor
            sCost = car.fBuildCost

            # Print off car info. The position needs to be increased by 1 to show the
            # object position and not the list position
            print(f"{iPositionInList+1} - {sMake} {sModel} {sVin} {sColor} ${sCost}")
    else:
        print("THERE ARE NO CARS!")


# Instantiate Vars for program to work
# List to keep track of each car build
listCarsBuilt = []
# Running total cost of cars built
fTotalCost = 0.0
# Running total sales of cars sold
fTotalSales = 0.0

# Get company name and if user wants to build a car
# If they do, they'll give a yes or y answer that we use to verify their desire for car building
sNameOfCarCompany = input("What is the car company name? ")
# Create the company object
oCompany = Company(sCompanyName=sNameOfCarCompany)
sBuildCar = input("Do you want to build a car? Y/N: ")[0].upper()

# While the user wants to keep building cars, help them build a car
while sBuildCar == "Y":
    # TODO remove this later
    print("Cool lets build a car")
    # end TODO

    # Get user inputs describing the car to be built
    sCarMake = input("\nWhat is the make of the car? ")
    sCarModel = input("What is the model of the car? ")
    sCarColor = input("What is the color of the car? ")
    sCarVin = input("What is the VIN of the car? ")
    sCarEngine = input("What engine is in the car? ")
    fTireSize = float(input("What is the size of the car's tires? "))
    fCostToBuild = float(input("What is the cost to build the car? "))

    # Build the car object from user input & add it into the built cars list
    oCar = Car(
        sMake=sCarMake,
        sModel=sCarModel,
        sColor=sCarColor,
        sVIN=sCarVin,
        sEngineDescription=sCarEngine,
        fTireSize=fTireSize,
        fBuildCost=fCostToBuild,
    )
    listCarsBuilt.append(oCar)

    # Update the costs of the company for the manufacturing of the car
    oCompany.changeCost(fBuildCosts=oCar.fBuildCost)

    # Check if the user wants to build any more cars
    sBuildCar = input("\nDo you want to build another car? Y/N: ")[0].upper()

sSellCars = input("\nDo you want to sell a car? Y/N: ")[0].upper()
# While the user wants to keep selling cars AND there are cars to sell, help them sell a car
while sSellCars == "Y" and listCarsBuilt:
    # Show the user what cars they can sell
    printCars(listCarsBuilt)

    # Ask the user which car they want to sell from the list previously shown
    iCarToSellPos = int(input("Which car would you like to sell? "))
    while iCarToSellPos <= 0 or iCarToSellPos > len(listCarsBuilt):
        iCarToSellPos = int(input("Sorry! That car doesn't exist.\nWhich car would you like to sell? "))

    # Get the sales price from the user and update the companies revenues for the sale of the car
    fSalesPrice = float(input("What is the sales price? "))
    oCompany.changeEarnings(fSalesEarnings=fSalesPrice)

    # Remove the car from the list since it sold and can't be sold again
    # The user will give the number position the objects are in and we have to convert this back to the actual
    # location in the list by subtracting 1
    listCarsBuilt.pop(iCarToSellPos - 1)
    sSellCars = input("\nDo you want to sell a car? Y/N: ")[0].upper()

# Print off any remaining cars and the company's metrics
printCars(listCarsBuilt)
if not listCarsBuilt:
    print("Congratulations! All cars have sold!")
print(f"\nInventory Costs: ${oCompany.getCost()}")
print(f"Sales Revenues: ${oCompany.getEarnings()}")
print(f"Profit: ${oCompany.getEarnings() - oCompany.getCost()}")
