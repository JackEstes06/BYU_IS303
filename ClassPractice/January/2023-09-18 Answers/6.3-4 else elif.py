# Else will run the code if the logical statement is not true
# note that once something is found true, the else WILL NOT run.

num1 = 3000
num2 = 20

if num1 == num2:
    print('They are equal')
else:
    print('they are not equal')

print("this will print no matter what, it is outside the if statement")

# else if, typed elif allows you to specify multiple conditions
if num1 == num2:
    print('They are equal')
elif num1 > num2:
    print('num 1 is greater than num2!')
else:
    print('num 1 is less than num2!')


# PRACTICE:
'''
    Ask the user to enter their favorite day of the week.
        If it is Monday, print "wow, early weekday"
        If it is Wednesday print "wow, midweek!"
        if it is Saturday print "weekend, woo!"
        if it is any other day, print "that day's pretty good too"
'''
sInput = input("What is your favorite day of the week? ")

if sInput == "Monday":
    print('wow, early weekday!')
elif sInput == "Wednesday":
    print("wow midweek")
elif sInput == "Saturday":
    print("weekend woo!")
else:
    print("That's pretty good too")


