# by combining comparisons with the if statement,
# you control what code gets executed

# Write a program that prints "congrats!"
# but only if num1 is not equal to num2

num1 = 10
num2 = 20

#structure of if statement:
'''
    must start with lowercase if
    then you must have a logical statement
        (something that results in TRUE or FALSE). Usually a comparison
    a colon : following the logical statement
    Then indent in (press tab) on the next line. Anything you want to only
    execute if the statement is true needs to be indented.

'''
if num1 == num2:
    print("congrats!")
    print("another line of congrats")


# Shorthand version:
if num1 != num2: print("congrats! shorthand") , print("another line of congrats shorthand")


# PRACTICE:
'''
    Check if a number stored in a variable is equal to 5.
    If it is, say "Wow it is equal to 5". No matter what the number
    is, print out the value of the number afterwards.
'''
iVarExample = 7
if iVarExample == 5:
    print("it is equal to 5")
print(iVarExample)
