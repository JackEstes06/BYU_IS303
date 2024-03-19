# Jack Estes
# IS303 Section 3
# 3/19/24
# Program that practices the basics of using a Pandas dataframe (df)

import pandas as pd

# import data from csv and create Pandas df based on the csv data
dfPersons = pd.read_csv(
    "practice_names.csv",
    # This would be used to organize by a person's name, but it isn't necessary atm
    # index_col="name",
)
# Output data as Pandas df to user (NOT NEEDED SO REMOVED)
# print(f'{dfPersons}\n\n')

# Print out specific column information
print(f'{dfPersons.city}\n')
print(f'{dfPersons[["name", "age"]]}\n')

# Update specific values & print
# Get the row where Joey Tribbiani shows up and update his salary
joey_row_index = dfPersons.index[dfPersons.name == 'Joey Tribbiani'][0]
dfPersons.at[joey_row_index, "salary"] = 56000
print(f'{dfPersons.iloc[joey_row_index]}\n')
# Get the row where Jane Smith shows up and update her age
jane_row_index = dfPersons.index[dfPersons.name == 'Jane Smith'][0]
dfPersons.at[jane_row_index, "age"] = 29
print(f'{dfPersons.iloc[jane_row_index]}\n')

# Filter data by age and multiple cities
filteredPersons = dfPersons.query(
    "age > 35 and "
    "(city == 'Boston' or city == 'Seattle' or city == 'San Francisco')"
)
print(f'{filteredPersons}\n')
# Sort data
print(f'{filteredPersons.sort_values(
    by=['salary'],
    ascending=[False]
)}')
