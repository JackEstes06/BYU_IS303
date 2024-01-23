# Jack Estes
# BYU IS303 Section 3
# Sample Program

# Grab input from user -> some inputs are type-casted to data types wanted
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
iAge = input("Enter your age in whole number years (ie. 24): ")
# Verify that the age input is an integer
while True:
    try:
        iAge = int(input("Enter your age in whole number years (ie. 24): "))
        break
    except ValueError:
        print("You entered a non integer value, try again.")
        continue

# Different ways to output name
print(sLastName + ", " + sFirstName)
print(sLastName, sFirstName)
print(sLastName, sFirstName, sep=", ", end="\n")
print("{last}, {first}".format(last=sLastName, first=sFirstName))

# Different ways to output age
print(str(iAge) + " years old")
# This format doesn't have to convert data
print("{age} years old".format(age=iAge))
