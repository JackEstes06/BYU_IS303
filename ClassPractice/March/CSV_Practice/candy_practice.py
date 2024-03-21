import pandas as pd

dfCandy = pd.read_csv("candy.csv")
print(dfCandy)
print(dfCandy.loc["Snickers"])
print(dfCandy.loc[["Snickers"]])
