# rounding
# you can use the function round() to round numbers
# round(number, decimal_place)

# round 7.8456 to the 3rd decimal place
print("rounding to the 3rd place", round(7.8456, 3))

# just remember that it rounds odd number up from .5
# and even numbers down from .5
# this is called Bankers rounding.
fOdd = 1.5
fEven = 2.5

print("rounding odd", round(fOdd))
print("rounding even", round(fEven))

# Be aware if this, but don't worry too much about it.

# Why? Isn't this dumb?
'''
    TL;DR: Always rounding from .5 means on average you round up more than you round down. Bankers Rounding gets around this.

    Bias Reduction: Traditional rounding (always rounding .5 up) can introduce an upward bias over large datasets,
        whereas bankers' rounding tends to reduce this bias by distributing half-roundings evenly between up and down.

    Fairness: In situations like financial transactions where rounding can benefit or penalize a party,
        bankers' rounding is seen as more neutral and fair.

    Statistical Robustness: Over large datasets, bankers' rounding helps in reducing the cumulative error,
        making statistical results slightly more robust.

    Prevents Encouraging Unwanted Behavior: In certain contexts, if rounding always goes up,
        it might encourage behaviors like always setting prices just a half unit lower than a full number to take advantage of the rounding.
'''
# Can I get around this?
''' Yes, you can write your own rounding function. But we won't cover that for another couple weeks or so.'''


# use negative numbers to round before the decimal point
# round 7879 to the 10s
print("rounding numbers to the left of the decimal", round(7879, -1))