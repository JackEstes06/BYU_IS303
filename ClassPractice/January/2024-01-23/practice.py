# Jack Estes
# BYU IS303 Section 3
# Class Practice - for each employee, get wages & hours

# Instantiate vars
iNumEmps = 0
fTotal = 0
fEmpTotal = 0

# Calculate the total & keep a running total
# Ensure user input is int
while True:
    try:
        iNumEmps = int(input("How many employees? "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again.")
        continue

# range(startVal, endVal, increment)
for iCount in range(0, iNumEmps):
    fWage = float(input("Enter employee hourly wage: "))
    fHours = float(input("Enter hours employee worked: "))

    fEmpTotal = round(fWage * fHours, 2)
    fTotal += fEmpTotal
    print("You earned ${empTotal}".format(empTotal=fEmpTotal))

print("Total wages are ${total}".format(total=fTotal))
