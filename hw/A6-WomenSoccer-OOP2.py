# Jack Estes
# BYU IS303 Section 3
# 2/26/24

import random


class SoccerTeam:
    # Constructor w/ default values if not given in the OG instantiation
    def __init__(self, teamName="", wins=0, losses=0, games=0, gf=0, ga=0):
        self.teamName = teamName
        self.wins = wins
        self.losses = losses
        self.totalGames = games
        self.goalsScored = gf
        self.goalsAllowed = ga
        self.winLossRatio = self.calc_win_loss_ratio()

    # Add a win to SoccerTeam.wins
    # Updates W/L Ratio after adding a win
    def new_win(self):
        self.wins += 1
        self.winLossRatio = self.calc_win_loss_ratio()

    # Add a loss to SoccerTeam.losses
    # Updates W/L Ratio after adding a loss
    def new_loss(self):
        self.losses += 1
        self.winLossRatio = self.calc_win_loss_ratio()

    # Outputs the SoccerTeams season status information
    # Info is team's name, their wins-loss and their W/L Ratio
    # Based on W/L Ratio, return a string that determines off-season qualifications and gives team feedback
    def season_status(self):
        homeTeamRecord = self.wins / (self.wins + self.losses)
        returnStmt = (f'Team Name: {self.teamName}\n'
                      f'Final season record {self.wins}-{self.losses}\n'
                      f'Total goals scored: {self.goalsScored} - Total goals allowed: {self.goalsAllowed}\n')
        if homeTeamRecord >= 0.75:
            returnStmt += "Qualified for the NCAA Women's Soccer Tournament"
        elif homeTeamRecord >= 0.5:
            returnStmt += "You had a good season"
        else:
            returnStmt += "Your team needs to practice!"
        return returnStmt

    # Calculate the SoccerTeam's W/L Ratio
    def calc_win_loss_ratio(self):
        if self.losses == 0:
            self.winLossRatio = 1.0
        else:
            self.winLossRatio = self.wins / (self.wins + self.losses)
        return round(self.winLossRatio, 2)


# Instantiate Vars
homeTeam = input("What is the name of your home team? ")
totalHomeGames = "Not set yet"

# Verify that the user input for iTotalHomeGames is cast-able to int
while not isinstance(totalHomeGames, int):
    try:
        totalHomeGames = int(input("How many games will they play this season? "))
    except ValueError:
        print("Enter a numerical value (i.e. '4' not 'four')")
        totalHomeGames = int(input("How many games will they play this season? "))

team1 = SoccerTeam(teamName=homeTeam, games=totalHomeGames)

print()
for games in range(0, team1.totalGames):
    awayTeam = input(f"Enter the name of the away team for game {games + 1}: ")
    homeTeamScore = random.randrange(1, 15)
    awayTeamScore = random.randrange(1, 15)
    # We hate ties, force someone to win
    while homeTeamScore == awayTeamScore:
        homeTeamScore = random.randrange(1, 15)
        awayTeamScore = random.randrange(1, 15)
    # Adjust goal totals for the team object
    team1.goalsScored = team1.goalsScored + homeTeamScore
    team1.goalsAllowed = team1.goalsAllowed + awayTeamScore
    if homeTeamScore > awayTeamScore:
        team1.new_win()
    else:
        team1.new_loss()
    print(f"{homeTeam} score: {homeTeamScore} {awayTeam} score: {awayTeamScore}")

# If the home team never plays, there will be an x/0 error. To avoid this we exit the program when totalHomeGames = 0
if totalHomeGames == 0:
    print("\nHome team didn't play this season. Try again with a team that actually plays lol.")
    exit()

print(f'\n{team1.season_status()}')
