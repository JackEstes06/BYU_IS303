# Inheritance practice
class Student:
    def __init__(self, name="", gender="", lunch="", mathScore=0, readingScore=0, writingScore=0):
        self.name = name
        self.gender = gender
        self.lunch = lunch
        self.mathScore = mathScore
        self.readingScore = readingScore
        self.writingScore = writingScore

    def calculatedGrade(self, outputInfo=True):
        score = (self.mathScore + self.readingScore + self.writingScore) / 3
        if outputInfo:
            print(f"Calculated Grade = {score}")
        return score


class WellFedStudent(Student):
    def __init__(self, name="", gender="", lunch="", mathScore=0, readingScore=0, writingScore=0):
        super().__init__(name=name, gender=gender, lunch=lunch,
                         mathScore=mathScore, readingScore=readingScore, writingScore=writingScore)

    def calculatedGrade(self, outputInfo=True):
        score = super().calculatedGrade(outputInfo=False) * 3
        if outputInfo:
            print(f"Calculated Grade = {score}")
        return score


oStudent1 = Student(name="Greg", gender="M", lunch="Standard", mathScore=80, readingScore=80, writingScore=80)
oStudent2 = WellFedStudent(name="Sandy", gender="F", lunch="BetterLunch", mathScore=80, readingScore=80, writingScore=80)
oStudent1.calculatedGrade()
oStudent2.calculatedGrade()

# -------------------------------------------------------------------------------------------------------------------- #

# Excel practice w/ pandas
import pandas as pd

studentList = []
df = pd.read_excel("study_performance.xlsx")
print(df)

for index, row in df.iterrows():
    name = row["name"]
    gender = row["gender"]
    lunch = row["lunch"]
    mathScore = row["math_score"]
    readingScore = row["reading_score"]
    writingScore = row["writing_score"]

    if lunch != "standard":
        studentList.append(
            Student(
                name=name,
                gender=gender,
                lunch=lunch,
                mathScore=mathScore,
                readingScore=readingScore,
                writingScore=writingScore
            )
        )
    else:
        studentList.append(
            WellFedStudent(
                name=name,
                gender=gender,
                lunch=lunch,
                mathScore=mathScore,
                readingScore=readingScore,
                writingScore=writingScore
            )
        )

for student in studentList:
    print(f"{student.name} is a {student.gender} that has a {student.lunch} lunch. "
          f"\nTheir calculated grade is: {round(student.calculatedGrade(outputInfo=False), 2)}\n")
