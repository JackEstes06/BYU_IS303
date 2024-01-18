######
## CHAPTER 3
######

######
## Documentation
######

# Author: Jacob Steffen

# Single line quote
''' type anything
    I want
    on multiple lines
'''

''' Multi
    Line
    quote
    
'''
"""
    Also 
    works
    with double quotes
"""

######
## DATA TYPES
######

# string: for storing text
myName = "Jacob Steffen"
myOtherName = 'Professor Steffen'

# integer (or int): Whole numbers, no decimals
thisIsAWholeNumber = 10

# float: number w/ decimals
ThisHasDecimals = 10.5

# boolean: True or False. 
booleanExample = True

# if you want to see what the data type is:
#print(type(variableName))

print(myName)

print(type(myName))
print(type(ThisHasDecimals))
# remember that python is dynamically typed! (instead of statically typed)

###
# PRACTICE #1
###
#   store an integer and a float in two separate variables. Print out their sum.
x = 23
y = 20.7

print(x + y)

# you could also store the sum of x and y in  their own variable
sum = x + y
print(sum)

######
## Naming Conventions
#####
# Remember, you can name it basically whatever you want (start with a letter or underscore though)
# But some code is more readable than other code
# see https://www.youtube.com/watch?v=-J3wNP6u5YU&ab_channel=CodeAesthetic

# camelCase
variableName = "something"
# sHungarian Notation
sVariableName = "something else"
iVariableName = 10
fVariableName = 1.2345

#######
## CHAPTER 4
######

######
## Functions
#######
# functions are prewritten code that you are "calling". You give it an input, and it will do something with that input.
# so far, we've seen type() and print()
print(myName)

# sometimes, functions can accept multiple inputs. Let's try it with print. 
print(myName,myOtherName, "something else")

# functions also can accept inputs if you name them.
# for print we can try sep = "" and end =""

print(myName, myOtherName, sep = "_")

######
## input
######
# when we want input from the user of the program, we can use input(), which 
# takes what the user types and puts it into a string

sUserInput = input("What is your favorite Food: ")
print(sUserInput)

###
# Practice #1
### 
#   Ask the user for their favorite food and then print out "This is your favorite food: x"
sUserFavoriteFood = input("pls tell me ur favorite food: ")
print("this is your favorite food:", sUserFavoriteFood)


######
## Converting Data Types
######

# Implicitly (e.g. you don't have to do anything)
# can change ints or floats to strings.
iIntExample = 10
print(iIntExample)

# can add float and int to make a float.
fFloatExample = 20.4

print(fFloatExample +iIntExample)
###
# PRACTICE 3
###
# ask the user for their favorite number, and add 2 to it and print it out
iFavoriteNumberInput = input("give me your favorite number: ")

# Here' I'm printing the data type of iFavoriteNumberInput
print(iFavoriteNumberInput)
print(type(iFavoriteNumberInput))
x = "2"

# trying to add 2 to favorite number and print it out
print(iFavoriteNumberInput + x)

#### Example with int() before the print
iFavoriteNumberInput = input("give me your favorite number: ")
iFavoriteNumberInput = int(iFavoriteNumberInput)
# trying to add 2 to favorite number and print it out
print(iFavoriteNumberInput + 2)


#### The best way!!!
iFavoriteNumberInput = int(input("give me your favorite number: "))

# trying to add 2 to favorite number and print it out
print(iFavoriteNumberInput + 2)




# Explicity convert (you need to call a function)
'''
    int(x)	    Converts x to an integer
    float(x)	Converts x to a floating-point number (decimals)
    str(x)	    Converts x to a string
    chr(x)	    Converts x to a character
'''


# Some functions are called by putting a . and then the function name.
# like at the end of a string, put .upper() or .lower()

print(myName.upper())

# string.format()
print("hello, {0}, is a {1} {2}".format("this", "great", "example"))

#####
## Escape Characters
#####

'''
    \'
    \"
    \\
    \n
    \t
'''
print('I\'m using single quotes so I need to use an escape character to display a single quote')


######
## concatenation
######

print("string 1" + "string 2")

###
# PRACTICE 4
###
'''
    Write a program that prompts the user for a first name,
    last name, street address, city, state, and the birth year of the individual.
    Calculate the age of the individual (or the age they'll turn this year). Print the concatenated full name
    all in upper case separated by a space. Print the address on a separate line.
    Print the city and state on another separate line separated by a tab.
    Make sure the state is all upper case. Print the calculated age in years on another
    separate line concatenated with "In 2020 ZZ was XX years old" -
    where ZZ is the first name and XX is the calculated age in years.
'''

# Note this is the same practice as from Chapter 4. See the video there.

