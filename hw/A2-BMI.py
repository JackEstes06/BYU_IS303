# Jack Estes
# BYU IS303 Section 3
# BMI Calculator

# Instantiate vars
fHeightInFeet = 0
fHeightInInches = 0
fWeightInPounds = 0
fBMIVal = 0

# Get user's name & body info
sFName = input("Enter your first name: ")
sLName = input("Enter your first name: ")
# Verify that the user input can be converted to an numbers
while True:
    try:
        iHeightInFeet = int(input("Enter your height in feet: "))
        break
    except ValueError:
        print("You entered a non-integer value, try again.")
        continue
while True:
    try:
        iHeightInInches = float(input("Enter your height in inches: "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again.")
        continue
