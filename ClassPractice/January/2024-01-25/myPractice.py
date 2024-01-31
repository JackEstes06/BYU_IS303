# Jack Estes
# BYU IS303 Section 3
# Class Practice - practice w/ loops

# Prompt user for # of grade
iNumGrades = 0
while True:
    try:
        iNumGrades = int(input("Enter the number of grades you want to avg: "))
        break
    except ValueError:
        print("Enter a numeric value (i.e. 4)")
        continue

# Gather all grade numbers
setTotalGrades = set()
iCurrGradeValue = 0
for grades in range(0, iNumGrades):
    while True:
        try:
            iCurrGradeValue = int(input("Enter the grade value: "))
            break
        except ValueError:
            print("Enter a numeric value (i.e. 94)")
            continue
    setTotalGrades.add(iCurrGradeValue)

# Calculate avg grade after dropping lowest grade
print("The avg grade before lowest is dropped is {avg}".format(
    avg=round((sum(setTotalGrades)/iNumGrades), 2)))
setTotalGrades.remove(min(setTotalGrades))
iAvgGrade = 0
for grades in setTotalGrades:
    iAvgGrade += grades
iAvgGrade /= (iNumGrades-1)

# Display the avg grade
print("The avg grade is {avg}".format(avg=round(iAvgGrade, 2)))

# >=90 A, >=80, otherwise C
if iAvgGrade >= 90:
    print("Your avg grade is an A")
elif iAvgGrade >= 80:
    print("Your avg grade is an B")
else:
    print("Your avg grade is an C")
