# We likely won't have time to get to these, but we can start practicing if we have time.


'''
    and     Every statement must be true
    or      At least one statement must be true
    not     negates a statement. put it before any logical statement
'''

# a semi-complex example we can work up to:

x = 5
y = 10
z = 15

if (x < y and y < z) or (x == 5 and z == 15):
    print("The conditions are met.")
else:
    print("The conditions are not met.")
