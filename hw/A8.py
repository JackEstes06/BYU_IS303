# Authors: Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian McFarland, Allen Schultz, Hayden Whalen Section 3
# Description: This program simulates a line of customers at a restaurant. It creates and uses 3 classes (inheritance
# involved). It then creates and iterates through a queue and a dictionary.

# Import random for use in code
import random


# Creates class Order
class Order:
    # Constructor to initialize instance variable as the return value from a method
    def __init__(self):
        self.burger_count = self.randomBurgers()

    # Method to return a random number
    def randomBurgers(self):
        return random.randint(1, 20)


# Creates class Person
def randomName():
    lstCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman",
                    "Carmen", "Invisible Swordsman", "Singing Bush"]

    return random.choice(lstCustomers)


class Person:
    # Constructor to initialize instance variable as the return value from a method
    def __init__(self):
        self.customer_name = randomName()

    # Method to return a random customer name from a list


# Creates class Customer that inherits from class Person
class Customer(Person):
    # Constructor to call super and initialize instance variable as an object of type Order
    def __init__(self):
        super().__init__()
        self.order = Order()


# This is the main program

# Creates an empty queue
queueLine = []

# Creates an empty dictionary
dictOrders = {}

# For loop to create 100 customer objects and append each one to the queue
for iCount in range(0, 100):
    oCustomer = Customer()
    queueLine.append(oCustomer)

# For loop to iterate through each customer in the queue
for oCustomer in queueLine:
    # If customer_name key already exists in dictionary, adds burger count to value
    if oCustomer.customer_name in dictOrders:
        dictOrders[oCustomer.customer_name] += oCustomer.order.burger_count
    # Else it creates a customer_name key and assigns the value of burger count
    else:
        dictOrders[oCustomer.customer_name] = oCustomer.order.burger_count

    # Deletes customer at front of queueLine
    queueLine.pop(0)

# Assigns dictionary sorted in descending burger count order to listSortedCustomers
listSortedCustomers = sorted(dictOrders.items(), key=lambda burgercount: burgercount[1], reverse=True)

# For loop to iterate through each customer in the sorted list
for oCustomer in listSortedCustomers:
    # Prints the customer name left adjusted and the customer burger count
    print(oCustomer[0].ljust(19), oCustomer[1])
