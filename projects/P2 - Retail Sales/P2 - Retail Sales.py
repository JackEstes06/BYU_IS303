# Jack Estes, Katelyn Hamilton, Hannah Larkin, Sebastian Mcfarland, Allen Schultz, Hayden Whalen
# IS303 Section 3
#
# Assume you are given a sample of sale data from an online retailer in the form of an excel file. The retailer wants
# your team to test how they could transfer their data into a postgres database and read data programmatically back
# from the database. You’ll use Pandas to read the data in, to transfer it to postgres, and to read it back from
# postgres to display a summary of different product categories.

import openpyxl
import sqlalchemy
import pandas as pd
import matplotlib.pyplot as plot

# Import data from excel file
# Data is organized as follows (not exact heading titles, some abbreviated):
# sale_id | fname_lname | product | qty_sold | sale_date | unit_price | total_price | age_group | gender | payment
retailDF = pd.read_excel("Retail_Sales_Data.xlsx")
nameDF = pd.DataFrame(retailDF.name)
fNameList = []
lNameList = []
for row in nameDF.iterrows():
    names = row[1].values[0].split("_")
    if len(names) > 1:
        fNameList.append(names[0])
        lNameList.append(names[1])
retailDF.__delitem__("name")
retailDF['FirstName'] = fNameList
retailDF['LastName'] = lNameList
# details = retailDF.loc["Morgan_Wilson"]
# print(details)
print(retailDF)
# print(retailDF.describe())

# Converts xlsx to cvs and keeps headers as they were originally
retailCSV = retailDF.to_csv("Retail_Sales_Data.csv", encoding="utf-8", index=True)
