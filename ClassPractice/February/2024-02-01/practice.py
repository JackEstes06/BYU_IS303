def calc_gpa(letter):
    if letter == "A":
        gpa = 4.0
    elif letter == "B":
        gpa = 3.0
    elif letter == "B":
        gpa = 2.0
    elif letter == "B":
        gpa = 1.0
    else:
        gpa = 0
    return gpa


letterGrade201 = input("What was your closest letter grade for IS201 (i.e. A or B): ").upper()
gpa201 = calc_gpa(letterGrade201)
letterGrade303 = input("What was your closest letter grade for IS303 (i.e. A or B): ").upper()
gpa303 = calc_gpa(letterGrade303)
letterGrade200 = input("What was your closest letter grade for ACC200 (i.e. A or B): ").upper()
gpa200 = calc_gpa(letterGrade200)

print("Avg gpa for those 3 classes were {gpa}".format(
    gpa=round((gpa201 + gpa303 + gpa200)/3, 2)
))
