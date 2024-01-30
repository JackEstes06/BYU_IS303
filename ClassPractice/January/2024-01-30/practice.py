# Jack Estes
# IS303 Section 3
# Class Practice - While Loops Practice

sCondition = input("Do you want to enter a grade? ").upper()[0]
iLowGrade = 0
iTotal = 0
iNumGrades = 0

# Get user inputted grades for as many as they want to avg
while sCondition == "Y":
    iGradeValue = int(input("Enter a grade value {count} (i.e. 91): ".format(count=iNumGrades)))
    if iNumGrades == 0:
        iLowGrade = iGradeValue
    if iGradeValue < iLowGrade:
        iLowGrade = iGradeValue

    iNumGrades += 1
    iTotal += iGradeValue
    sCondition = input("Do you want to enter a grade? ").upper()[0]

# Output avg grades w/ & w/o lowest grade
print("Lowest grade was {lowest}. Avg w/ lowest grade included was {avg}."
      .format(lowest=iLowGrade, avg=round(iTotal/iNumGrades, 2)))
# Remove the lowest grade
iTotal -= iLowGrade
iNumGrades -= 1
print("Avg grade was after dropping the lowest was {avg}."
      .format(avg=round(iTotal/iNumGrades, 2)))
