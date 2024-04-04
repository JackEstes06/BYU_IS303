# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
# Project 2 -

# Useful imports
import sqlalchemy
from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plot

# Defines the connection parameters
database_name = "sales"
db_user = "postgres"
db_password = "3210Jte10!"
db_host = "localhost"
db_port = "5432"

# Obtains user input
sUserInput = input("If you want to import data, enter 1. "
                   "If you want to see summaries of stored data, enter 2. "
                   "Enter any other value to exit the program: ")

# Reads excel file using pandas
dfSales = pd.read_excel("Retail_Sales_Data.xlsx")

# Connects to postgres database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
conn = engine.connect()

# If statement
if sUserInput == "1":
    # Splits 'name' column into 'first_name' and 'last_name'
    dfSeparatedNames = dfSales["name"].str.split("_", expand=True)

    # Assign 'first_name' and 'last_name' columns directly
    dfSales['first_name'] = dfSeparatedNames[0]
    dfSales['last_name'] = dfSeparatedNames[1]

    # Drop the original 'name' column
    dfSales.drop(columns=["name"], inplace=True)

    # Categories dictionary
    productCategoriesDict = {
        'Camera': 'Technology',
        'Laptop': 'Technology',
        'Gloves': 'Apparel',
        'Smartphone': 'Technology',
        'Watch': 'Accessories',
        'Backpack': 'Accessories',
        'Water Bottle': 'Household Items',
        'T-shirt': 'Apparel',
        'Notebook': 'Stationery',
        'Sneakers': 'Apparel',
        'Dress': 'Apparel',
        'Scarf': 'Apparel',
        'Pen': 'Stationery',
        'Jeans': 'Apparel',
        'Desk Lamp': 'Household Items',
        'Umbrella': 'Accessories',
        'Sunglasses': 'Accessories',
        'Hat': 'Apparel',
        'Headphones': 'Technology',
        'Charger': 'Technology'}

    # Fixes the categories
    dfSales["category"] = dfSales["product"].map(productCategoriesDict)

    # Writes to SQL
    dfSales.to_sql("sale", engine, if_exists='replace', index=False)

    # Prints message to user
    print("You've imported the excel file into your postgres database.")

elif sUserInput == "2":
    # Get unique product categories
    print("The following are all the categories that have been sold:")
    dfImported = pd.read_sql_query("SELECT * FROM sale", engine)
    count = 1
    for category in dfImported["category"].unique():
        print(f"{count}: {category}")
        count += 1

    # Prints message to user
    categoryToSum = int(input("\nPlease enter the number of the category you want to see summarized: "))

    # Dictionary to assign each category value a numerical key
    categoryNameDict = {
        1: "Technology",
        2: "Apparel",
        3: "Accessories",
        4: "Household Items",
        5: "Stationery",
    }

    # Filter the data to what the user wants information on
    category = categoryNameDict[categoryToSum]
    dfImportedFiltered = dfImported.query(f"category == '{category}'")
else:
    # Prints message to user
    print("Closing the program.")
