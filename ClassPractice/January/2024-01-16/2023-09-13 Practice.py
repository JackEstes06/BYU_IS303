######
## CHAPTER 3
######

######
## Documentation
######

# Single line quote

''' Multi
    Line
    quote
    
'''

""""Also 
    works
    with double quotes """

######
## DATA TYPES
######

# string: for storing text

# integer (or int): Whole numbers, no decimals

# float: number w/ decimals

# boolean: True or False. 

# if you want to see what the data type is:
#print(type(variableName))

# remember that python is dynamically typed! (instead of statically typed)

###
# PRACTICE #1
###
#   store an integer and a float in two separate variables. Print out their sum.


######
## Naming Conventions
#####
# Remember, you can name it basically whatever you want (start with a letter or underscore though)
# But some code is more readable than other code
# see https://www.youtube.com/watch?v=-J3wNP6u5YU&ab_channel=CodeAesthetic

# camelCase
# sHungarian Notation


#######
## CHAPTER 4
######

######
## Functions
#######
# functions are prewritten code that you are "calling". You give it an input, and it will do something with that input.
# so far, we've seen type() and print()

# sometimes, functions can accept multiple inputs. Let's try it with print. 

# functions also can accept inputs if you name them. for print we can try sep = "" and end =""


######
## input
######
# when we want input from the user of the program, we can use input(), which 
# takes what the user types and puts it into a string

###
# Practice #1
### 
#   Ask the user for their favorite food and then print out "This is your favorite food: x"

######
## Converting Data Types
######

# Implicitly (e.g. you don't have to do anything)
# can change ints or floats to strings.
print("something", 3.14)

# can add float and int to make a float.

###
# PRACTICE 3
###

# ask the user for their favorite number, and add 2 to it and print it out

# Explicity convert (you need to call a function)
'''
    int(x)	    Converts x to an integer
    float(x)	Converts x to a floating-point number (decimals)
    str(x)	    Converts x to a string
    chr(x)	    Converts x to a character
'''


# Some functions are called by putting a . and then the function name.
# like at the end of a string, put .upper() or .lower()


# string.format()
# "hello, {0}, is a {1} {2}".format("this", "great", "example")

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

######
## concatenation
######


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


