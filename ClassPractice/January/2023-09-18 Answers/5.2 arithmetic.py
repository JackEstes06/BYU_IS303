# addition: +
print("addition", 2 + 5)

# subtraction -
print("subtraction", 2 - 5)

# multiplication *
print("multiplication", 2 * 5)

# division: /  
''' note this is a forward slash: /
    we used back slash before for escape characters: \ like \'
    the way I remember is that we read from left to right.
    in a forward slash it is like the line's head is leaning forward /
    in a back slash it's like the line is leaning backwards \ '''
print("division", 2 / 5)

# exponentiation: **
''' note, some other languages use ^ instead of **.
    That is something else entirely in python (Bitwise OR, don't worry about it)
    so don't use it for exponentiation  '''
print("exponentiation", 2 ** 5)

# Modulus: %
''' modulus gives you the remainder from dividing two numbers together
    Ex. 6 / 2 evenly divides into 3, so there is 0 remaining
    But 7 / 2 doesn't evenly divides. 3 2's can fit into 7, with one left over
    so 7 % 2 would give an answer of 1. '''

print("Modulus, no remainders", 10 % 2)
print("Modulus, some remainders:", 25 % 7)

#note if you use % with something bigger on the right side, it'll just give you the number
print("Modulus, big right side", 10 % 12)

# Floor Division: //
''' Same as division, but will round down to the nearest whole number
    Ex. 5 / 2 = 2.5 but 5 // 2 = 2. You can think of it chopping off the
    decimals, but just beware that if you're working with negative numbers
    it is still rounding down. try it with -5 / 2 and -5 // 2'''
print("floor division", -5 //2)

# PRACTICE 1: 
''' Imagine you're a teacher, and you have a jar of candies
    that you want to distribute equally among your students.
    Candies can't be cut, you can only give whole candies.

    Scenario:

    You have 47 candies.
    You have 8 students.
    You want to know how many candies each student will get
    if they are distributed evenly.

    Make variables representing the number of candies
    and the number of students.
    Print out how many candies each student can get '''
iCandy = 47
iStudent = 8
# use floor division to end up with integer 
iCandyPerStudent = iCandy // iStudent
print(iCandyPerStudent)

# Practice 2:
''' The exact same scenario as practice 1, but print out
    how many candies you will have left after distributing the candies
    out equally among the 8 students.   '''
# use modulus to get remainder
iCandyLeftOvers = iCandy % iStudent
print(iCandyLeftOvers)