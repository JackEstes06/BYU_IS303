# Jack Estes
# BYU IS303 Section 3
# Python Installation & Conversion Program

# This program prompts the user for the cose of a house & converts it to
# Taiwanese Dollars from U.S. Dollars

# Instantiate Variables
# Conversion rate from Google as of Jan 20, 2024
fConversionRate = 31.40
fHouseCost = 0.0
fTaiwaneseDollars = 0.0

# Verify that the house cost input is a numeric value
while True:
    try:
        fHouseCost = float(input("Enter the cost of an avg 4 bedroom house in Bentonville, AR: "))
        break
    except ValueError:
        print("You entered a non-numeric value, try again using numbers only.")
        continue

# Convert house cost to new taiwanese dollars
fTaiwaneseDollars = float(fConversionRate*fHouseCost)

# Output
print("The cost of a ${house} bedroom home in Bentonville, AR in "
      "New Taiwanese Dollars is\n${taiwan:.2f}"
      .format(house=fHouseCost, taiwan=fTaiwaneseDollars))
