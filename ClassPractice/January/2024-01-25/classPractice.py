# Jack Estes
# BYU IS303 Section 3
# Class Practice - practice w/ loops

# Prompt user for # of grade
# Gather all grade numbers
# Calculate avg grade after dropping lowest grade
# Display the avg grade
# >=90 A, >=80, otherwise C

iTotal = 0
iLowGrade = 0
iNumGrades = int(input("Enter the number of grades: "))

for iCount in range(0, iNumGrades):
    iCurrGrade = int(input("Enter grade " + str(iCount + 1) + ": "))

    if iCount == 0:
        iLowGrade = iCurrGrade
    if iCurrGrade < iLowGrade:
        iLowGrade = iCurrGrade
# Debugger practice - use breakpoint here
    iTotal += iCurrGrade

iTotal -= iLowGrade
iAvgGrade = int(iTotal/(iNumGrades - 1))
