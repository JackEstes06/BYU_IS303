# Jack Estes
# BYU IS303 Section 3
# Women's Soccer Program - Program that asks about a home women’s
#   soccer team, how many games they played in a season, and then
#   displays the scores of each game as well as the overall record
#   of the home team for the season.

import random

# Instantiate Vars
homeTeam = input("What is the name of your home team? ")
homeGamesWon = 0
totalHomeGames = "Not yet set"

# Verify that the user input for iTotalHomeGames is cast-able to int
while not isinstance(totalHomeGames, int):
    try:
        totalHomeGames = int(input("How many games will they play this season? "))
    except ValueError:
        print("Enter a numerical value (i.e. '4' not 'four')")
        totalHomeGames = int(input("How many games will they play this season? "))

for games in range(0, totalHomeGames):
    awayTeam = input(f"Enter the name of the away team for game {games+1}: ")
    homeTeamScore = random.randrange(1, 15)
    awayTeamScore = random.randrange(1, 15)
    while homeTeamScore == awayTeamScore:
        homeTeamScore = random.randrange(1, 15)
        awayTeamScore = random.randrange(1, 15)
    if homeTeamScore > awayTeamScore:
        homeGamesWon += 1
    print(f"{homeTeam} score: {homeTeamScore} {awayTeam} score: {awayTeamScore}")

# If the home team never plays, there will be a x/0 error. To avoid this we exit the program when totalHomeGames = 0
if totalHomeGames == 0:
    print("Home team didn't play this season. Try again with a team that actually plays lol.")
    exit()

homeTeamRecord = homeGamesWon / totalHomeGames
print(f"{homeTeam} went {homeGamesWon}-{totalHomeGames-homeGamesWon}")
if homeTeamRecord >= 0.75:
    print("Qualified for the NCAA Women's Soccer Tournament")
elif homeTeamRecord >= 0.5:
    print("You had a good season")
else:
    print("Your team needs to practice!")
