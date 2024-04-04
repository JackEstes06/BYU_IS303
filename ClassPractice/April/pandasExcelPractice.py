# Jack Estes
# 4/4/2024
# Class Practice

import os
import platform


def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


clear_screen()

import pandas as pd
import matplotlib as plot
import sqlalchemy
from sqlalchemy import create_engine, text
import psycopg2

# Define database connection params
db_name = "baseball"
db_user = "postgres"
db_password = "3210Jte10!"
db_host = "localhost"
db_port = "5432"

# Connect to Postgres DB
db_engine = sqlalchemy.create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
db_connection = db_engine.connect()

# Import File for DB
dfImportFile = pd.read_excel("mlb.xlsx")
# Convert pandas dataframe to postgres table
#   - Index false doesn't add an automatically generated PK
dfImportFile.to_sql("mlb", db_engine, if_exists='replace', index=False)


