import pandas as pd

# Create data personally
dctCandy = {
    "Description": ["SNICKERS", "KIT KAT", "SKITTLES"],
    "Calories": [280, 218, 81],
    "Fat_Content": [11, 11, 15]
}

dfCandy = pd.DataFrame(dctCandy)
dfCandy = dfCandy.sort_values(
    by=['Fat_Content', 'Description'],
    ascending=[True, True],
)
print(f'{dfCandy}\n')
print(f'{dfCandy["Description"]}\n')
print(f'{dfCandy[["Description", "Fat_Content"]]}\n\n\n')


# Extract data from spreadsheet
dfTeams = pd.read_csv(
    "pandasPractice.csv",
    index_col="Team",
)
print(dfTeams)
