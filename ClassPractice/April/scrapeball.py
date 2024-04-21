# Make sure you already installed requests and beautifulsoup4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
# You will need to pip install sqlalchemy
import sqlalchemy
# You will need to pip install sqlalchemy_utils
from sqlalchemy_utils import database_exists, create_database
today = datetime.today().strftime('%m-%d-%Y')

# define the connection parameters:
database_name = "baseball"
db_user = "postgres"
db_password = "3210Jte10!"
db_host = "localhost"
db_port = "5432"

# Connect to the PostgreSQL database
engine = sqlalchemy.create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{database_name}')
# If the database does not exist, then use SQLAlchemy to create it with create_database
# engine.url contains all of the needed information above to connect with the server and database
if not database_exists(engine.url):
    create_database(engine.url)
drop_table_query = sqlalchemy.text("DROP TABLE IF EXISTS mlb_games")
conn = engine.connect()
conn.execute(drop_table_query)
conn.commit()
conn.close()

# BTW, ESPN blocks scraping so we are using the link below
# Send a GET request to the webpage
url = 'https://www.baseball-reference.com/boxes/'
response = requests.get(url)
# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')
dictGames = {}
alGames = []

# Locate the elements containing the games, team names, and scores
# Note: These class names are placeholders; you'll need to inspect the webpage to find the actual class names or identifiers
games = soup.find_all('div', class_='game_summary')  # Placeholder class name
for game in games:
    # Create variables to hold the data
    team_name_win = ''
    team_name_lose = ''
    # I set these to -1 because 0 is a valid score
    score_win = -1
    score_lose = -1
    # get the HTML table that has all of the games and scores
    teams = game.find_all('table', class_='teams')  # Placeholder class name
    # Process the table rows (tr)  within the table
    # the winner class and the loser class has the team names and scores
    for team_names in teams:
        winner = game.find_all('tr', class_='winner')  # Placeholder class name
        loser = game.find_all('tr', class_='loser')  # Placeholder class name
        # Get the wining team name and score (class is right)
        # The a tag has the name and the td tag has the score
        for team1 in winner:
            team_name_win = team1.find_all('a')
            score_win = team1.find_all('td', class_='right')
        # Get the losing team name and score (class is right)
        # The a tag has the name and the td tag has the score
        for team2 in loser:
            team_name_lose = team2.find_all('a')
            score_lose = team2.find_all('td', class_='right')
        # If you used contents attribute then you would return list like ['Detroit Tigers']
        # We add a W which means won
        print(team_name_win[0].text, "-", score_win[0].text, " W ")
        print(team_name_lose[0].text, "-", score_lose[0].text)
        # Add a blank line - could have added \n above
        print()
        # Add record to list containing game information from scraped data (W - means win)
        alGames.append([today, team_name_win[0].text, score_win[0].text, "W", team_name_lose[0].text, score_lose[0].text])
# Create dataframe using the nested lists and specify the column names
df = pd.DataFrame(alGames, columns=['date', 'winning_team', "winning_score", "type", "losing_Team", "losing_Score"])
# Display data
print(df)
# Write the data from the dataframe to a table mlb_games
# Create the table if it doesn't exist and append the data to it
# This way you could run this every day
# Generate a primary key (index)
df.to_sql('mlb_games', engine, if_exists='append', index=True)
print("You've saved the scraped data to your postgres database.")