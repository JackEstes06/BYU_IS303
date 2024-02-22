# Jack Estes
# BYU IS303 Section 3
# Class Practice - Inheritance

# Program that tracks a student & their faculty mentor
# Student: fname, lname, gpa
# Faculty: fname, lname, deptName

# Base class for peoples to instantiate later
class Person:
    def __init__(self, fName="", lName="", dog=""):
        self.fName = fName
        self.lName = lName
        # private parameter, not every person has a dog but could
        self.__dog = dog

    def personInfo(self):
        return f'{self.fName} {self.lName}'


# Student inherits from person
class Student(Person):
    def __init__(self, fName="", lName="", gpa=0.0):
        super().__init__(fName, lName)
        self.gpa = gpa

    def studentInfo(self):
        return f'{self.personInfo()} has a {self.gpa} gpa'


# Faculty inherits from person
class Faculty(Person):
    def __init__(self, fName="", lName="", deptName=""):
        super().__init__(fName, lName)
        self.dept = Department(deptName)
        self.studentList = []

    def facultyInfo(self):
        return f'{self.personInfo()} works in the {self.dept.deptName} dept.'


class Department:
    def __init__(self, deptName):
        self.deptName = deptName


facultyMember1 = Faculty("Greg", "Anderson", "IS")
student1 = Student("Jack", "Estes", 2.69)
print(facultyMember1.facultyInfo())
print(student1.studentInfo())
