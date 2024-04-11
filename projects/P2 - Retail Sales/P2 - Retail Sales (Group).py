# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
# Project 2 -

# Useful imports
import sqlalchemy
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
engine.connect()

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


def dbDataInput():
    # Splits 'name' column into 'first_name' and 'last_name'
    dfSeparatedNames = dfSales["name"].str.split("_", expand=True)

    # Assign 'first_name' and 'last_name' columns directly
    dfSales.insert(1, 'first_name', dfSeparatedNames[0])
    dfSales.insert(2, 'last_name', dfSeparatedNames[1])
    # dfSales['first_name'] = dfSeparatedNames[0]
    # dfSales['last_name'] = dfSeparatedNames[1]

    # Drop the original 'name' column
    dfSales.drop(columns=["name"], inplace=True)

    # Fixes the categories
    dfSales["category"] = dfSales["product"].map(productCategoriesDict)

    # Writes to SQL
    dfSales.to_sql("sale", engine, if_exists='replace', index=False)


def displayDBDataInfo():
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

    # Obtains category name from user inputted number
    category = categoryNameDict[categoryToSum]

    # Obtains category that user inputted
    dfImportedFiltered = dfImported.query(f"category == '{category}'")

    # Calculate and display the sum of total sales
    totalSales = dfImportedFiltered["total_price"].sum()
    print(f"Total sales for {category}: ${totalSales:,.2f}")

    # Calculate and display the average sale amount
    avgSales = dfImportedFiltered["total_price"].mean()
    print(f"Average sale amount for {category}: ${avgSales:,.2f}")

    # Calculate and display the total units sold
    totalUnits = dfImportedFiltered["quantity_sold"].sum()
    print(f"Total units sold for {category}: {totalUnits}")

    # Creates and displays bar chart
    # Groups by product and calculates total sales for each
    productCounts = dfImportedFiltered.groupby("product")["total_price"].sum()
    # Specifies as bar chart
    productCounts.plot(kind="bar")
    # Creates title
    plot.title("Total Sales in " + category)
    # Creates x-axis label as "Product"
    plot.xlabel("Product")
    # Creates y-axis label as "Total Sales"
    plot.ylabel("Total Sales")
    # Displays bar chart
    plot.show()


# If statement to see what user wants to do
# Input the data regardless of user input so that the program never fails
dbDataInput()
if sUserInput == "1":
    # Prints message to user
    print("You've imported the excel file into your postgres database.")
if sUserInput == "2":
    displayDBDataInfo()
else:
    # Prints message to user
    print("Closing the program.")

# Close database connection
engine.dispose()
