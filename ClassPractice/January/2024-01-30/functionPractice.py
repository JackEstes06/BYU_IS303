# Jack Estes
# IS303 Section 3
# Class Practice - Practice w/ Functions

from random import randint

# scripture = "By the power of the Holy Ghost ye may know the truth of all things"
# print(scripture.replace("ye", "Section 3").lower())
#
# print(max(654, 3544, 12, 67))
# print("Random number = {rand}".format(
#     rand=randrange(1,101)
# ))

# Random number guessing game from 1-50
# User gets unlimited guesses w/ hints if too low/high
x = 1
y = 51
iNumGuesses = 1
iNumToGuess = randint(x, y)
iUserGuess = int(input("Guess a number from {x} to {y}: ".format(
    x=x,
    y=y-1
)))

while iUserGuess != iNumToGuess:
    sHint = "Low"
    if iUserGuess > iNumToGuess:
        sHint = "High"
    iUserGuess = int(input("Too {hint}. Guess another number from {x} to {y}: ".format(
        hint=sHint,
        x=x,
        y=y
    )))
    iNumGuesses += 1

print("Correct! It took you {num} tries".format(num=iNumGuesses))
