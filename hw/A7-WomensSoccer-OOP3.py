# Jack Estes
# BYU IS303 Section 3
# 2/22/24


# needed to generate random scores
import random


# Soccer Team object w/ all its defining attributes.
class SoccerTeam:
    def __init__(self, teamName="", wins=0, losses=0, goalsScored=0, goalsAllowed=0):
        self.teamName = teamName
        self.wins = wins
        self.losses = losses
        self.goalsScored = goalsScored
        self.goalsAllowed = goalsAllowed

    # generates the score with the standard chance
    def generateScore(self):
        return random.randint(0, 4)

    def updateGoalsScoredAndGoalsAllowed(self, scored=0, allowed=0):
        self.goalsScored += scored
        self.goalsAllowed += allowed

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    # depending on the win rate, display different final messages.
    def seasonStatus(self):
        if self.wins / (self.wins + self.losses) >= .75:
            message = f"Qualified for the NCAA Women's Soccer Tournament!"
        elif self.wins / (self.wins + self.losses) >= .5:
            message = f"You had a good season."
        else:
            message = f"Your team needs to practice!"
        return message


# Sponsored Soccer Team. Inherits everything and adds a sponsor to the object
class SponsoredTeam(SoccerTeam):
    def __init__(self, sponsorName="", teamName="", wins=0, losses=0, goalsScored=0, goalsAllowed=0):
        super().__init__(teamName, wins, losses, goalsScored, goalsAllowed)
        self.sponsorName = sponsorName

    # Override generateScore method from parent
    def generateScore(self):
        return random.randint(1, 4)

    # Override seasonStatus method from parent
    # Depending on the win rate, display different final messages.
    def seasonStatus(self):
        if self.wins / (self.wins + self.losses) >= .75:
            message = f"Qualified for the NCAA Women's Soccer Tournament! {self.sponsorName} is very happy."
        elif self.wins / (self.wins + self.losses) >= .6:
            message = f"{self.sponsorName} thinks you had a good season but hopes you can do better."
        else:
            message = f"You are in danger of {self.sponsorName} dropping you.."
        return message


# Class that creates and stores 2 soccer teams and their respective scores
class Game:
    def __init__(self, home=SoccerTeam(), away=SoccerTeam(), homeScore=0, awayScore=0):
        self.homeTeam = home
        self.homeScore = homeScore
        self.awayTeam = away
        self.awayScore = awayScore

    # Gets the scores of each team and generates them and outputs a message defining the game outcome
    # This also updates wins/losses and goals scored/allowed for both teams
    def gameStatus(self, hScore=0, aScore=0, updateScores=False):
        self.homeScore = hScore
        self.awayScore = aScore

        # Update scores is off by default. This is so you can come back later and check old games and see their status
        # without updating each soccer teams actual information (we don't want to update if they aren't new games)
        if updateScores:
            # Update both team's goalsScored & goalsAllowed variables
            self.homeTeam.updateGoalsScoredAndGoalsAllowed(scored=self.homeScore, allowed=self.awayScore)
            self.awayTeam.updateGoalsScoredAndGoalsAllowed(scored=self.awayScore, allowed=self.homeScore)

        # Update both team's wins & losses. No ties are allowed but that's taken care of before getting here
        if hScore > aScore:
            self.homeTeam.addWin()
            self.awayTeam.addLoss()
        else:
            self.awayTeam.addWin()
            self.homeTeam.addLoss()

        # Return status of game
        return f"|{self.homeTeam.teamName}| {self.homeScore}-{self.awayScore} |{self.awayTeam.teamName}|"


# get the inputs
sHomeTeamName = input("Enter the name of your team (the home team): ")
sIsSponsoredTeam = input("If your team is sponsored, enter the name of the sponsor. Otherwise enter N: ")
iNumGamesPlayed = int(input("Enter the number of teams that " + sHomeTeamName + " will play (1-10): "))

# creates a soccerTeam object and stores it in the variable homeTeam
if sIsSponsoredTeam.upper() != "N":
    homeTeam = SponsoredTeam(teamName=sHomeTeamName, sponsorName=sIsSponsoredTeam)
else:
    homeTeam = SoccerTeam(teamName=sHomeTeamName)

# this is creating an empty list for the away teams and an empty list for the games. We need to create the list
# outside the loop so it doesn't keep getting overwritten. Then in the loop, we just append to the list.
opponentTeamsList = []
gamesList = []

# run the loop for however many times the user entered
for game in range(1, iNumGamesPlayed + 1):
    # get away team name
    sAwayTeamName = input(f"Enter the name of the away team for game {game}: ")

    # make the away team object. 50/50 chance of being sponsored or normal:
    if random.randint(1, 100) % 2 == 0:
        awayTeam = SponsoredTeam(teamName=sAwayTeamName, sponsorName="Some Dirtbag from the U of U")
    else:
        awayTeam = SoccerTeam(teamName=sAwayTeamName)

    # generate scores for both teams, sponsored teams have higher chances of winning
    # no ties allowed
    homeTeamScore = homeTeam.generateScore()
    awayTeamScore = awayTeam.generateScore()
    while homeTeamScore == awayTeamScore:
        homeTeamScore = homeTeam.generateScore()
        awayTeamScore = awayTeam.generateScore()

    # Create a soccer game between 2 teams
    sGame = Game(home=homeTeam, away=awayTeam)
    # gameStatus automatically updates both teams' goals scored/allowed and wins/losses
    # gameStatus also prints the scores for each team & stores each one's scores into their respective vars in the class
    print(sGame.gameStatus(hScore=homeTeamScore, aScore=awayTeamScore, updateScores=True))
    opponentTeamsList.append(awayTeam)
    gamesList.append(sGame)

# At the end of the loop display: team name, season record, goals score/allowed, and the season Status.
print(f"\nTeam Name: {homeTeam.teamName}")
print(f"Final season record: {homeTeam.wins} - {homeTeam.losses}")
print(f"Total goals scored: {homeTeam.goalsScored} - Total goals allowed: {homeTeam.goalsAllowed}")
print(homeTeam.seasonStatus())

# Select a previously played game and print its result on screen
gameSelector = 0
while gameSelector != "exit":
    gameSelector = input(
        f"\nEnter in a game number between 1 and {iNumGamesPlayed} to see the stats of that game. "
        f"Otherwise type exit: ")

    if gameSelector.isdigit() and int(gameSelector) <= iNumGamesPlayed:
        gameSelector = int(gameSelector)
        # Returns gameStatus method on the specified game!
        print(gamesList[gameSelector - 1].gameStatus(
            hScore=gamesList[gameSelector - 1].homeScore,
            aScore=gamesList[gameSelector - 1].awayScore,
        ))
    elif gameSelector != "exit":
        print(f"Enter a value between 1 and {iNumGamesPlayed}")
