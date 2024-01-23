# Jack Estes
# BYU IS303 Section 3
# BMI Calculator

# Instantiate vars
iHeightInFeet = 0
fHeightInInches = 0
fWeightInPounds = 0
fBMIVal = 0
sBMIType = "Normal Weight"

# Get user's name & body info
sFName = input("Enter your first name: ")
sLName = input("Enter your first name: ")
# Verify that the user input can be converted to an numbers
while True:
    try:
        iHeightInFeet = int(input("Enter the feet portion of your height: "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again.")
        continue
while True:
    try:
        fHeightInInches = float(input("Enter the inches portion of your height: "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again.")
        continue
while True:
    try:
        fWeightInPounds = float(input("Enter your weight in pounds: "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again.")
        continue

# Calculate BMI & output to user
# Convert height to total inches
fHeightInInches += (iHeightInFeet*12)
# There are two ways to calculate BMI, one of the below lines is commented out since we only need 1
fBMIVal = fWeightInPounds/(fHeightInInches ** 2) * 703
# fBMIVal = ((fWeightInPounds/fHeightInInches)/fHeightInInches) * 703
# Determine BMI Type based on BMI Value
if fBMIVal < 18.5:
    sBMIType = "Underweight"
elif 18.5 <= fBMIVal < 25:
    sBMIType = "Normal Weight"
elif 25 <= fBMIVal < 30:
    sBMIType = "Overweight"
else:
    sBMIType = "Obese"

print("{fName} {lName}\nhas a BMI of {bmiVal} and is {bmiType}".format(
    fName=sFName,
    lName=sLName,
    bmiVal=round(fBMIVal,2),
    bmiType=sBMIType
))
