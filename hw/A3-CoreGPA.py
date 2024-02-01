# Jack Estes
# IS303 Section 3
# Prompts the user for inputs relating to IS Core requirements
# and gives the chances of getting into the IS program based on
# what was given.

# Mapped values of each letter grade and its value
gpaValues = {
    "A": 4.0, "A-": 3.7,
    "B+": 3.4, "B": 3.0, "B-": 2.7,
    "C+": 2.4, "C": 2.0, "C-": 1.7,
    "D+": 1.4, "D": 1.0, "D-": 0.7,
    "E": 0
}
# Predetermined weights of each core requirement
fIS201Weight = 0.30
fIS303Weight = 0.30
fAcc200Weight = 0.05
fOverallGPAWeight = 0.12
fLast30GPAWeight = 0.18
fEssayWeight = 0.05

# Get variable inputs from user
sIS201LetterGrade = input("What letter grade did you get for IS201 (i.e. A-)? ").upper()
sIS303LetterGrade = input("What letter grade did you get for IS303 (i.e. A-)? ").upper()
sAcc200LetterGrade = input("What letter grade did you get for ACC200 (i.e. A-)? ").upper()
fOverallGPA = float(input("What is your current overall GPA? "))
fLast30GPA = float(input("What is the GPA from your most recent 30 credits? "))
iEssayScore = int(input("What will you score on the IS application essays (whole numbers - scored 0 to 4)? "))

# Calculate weighted application GPA & output to user
fApplicationGPA = round(
        (gpaValues.get(sAcc200LetterGrade) * fAcc200Weight)
        + (gpaValues.get(sIS201LetterGrade) * fIS201Weight)
        + (gpaValues.get(sIS303LetterGrade) * fIS303Weight)
        + (fOverallGPA * fOverallGPAWeight)
        + (fLast30GPA * fLast30GPAWeight)
        + (iEssayScore * fEssayWeight), 3
)
print("Total Applying GPA is {gpa}".format(
    gpa=fApplicationGPA
))

# Display chances of making it into the IS Core
if fApplicationGPA >= 3.8:
    print("Chances are very good")
elif fApplicationGPA >= 3.5:
    print("Chances are good")
elif fApplicationGPA >= 3.2:
    print("Chances are so-so")
else:
    print("You might want to retake IS201 and/or IS303")
