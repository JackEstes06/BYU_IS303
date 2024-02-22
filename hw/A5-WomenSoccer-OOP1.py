# Jack Estes
# BYU IS303 Section 3
# 2/16/24

class SoccerTeam:
    # Constructor w/ default values if not given in the OG instantiation
    def __init__(self, teamName="", wins=0, losses=0, gf=0, ga=0):
        self.teamName = teamName
        self.wins = wins
        self.losses = losses
        self.goalsScored = gf
        self.goalsAllowed = ga
        self.winLossRatio = self.calc_win_loss_ratio()

    # Add a win to SoccerTeam.wins
    def new_win(self):
        self.wins += 1

    # Add a loss to SoccerTeam.losses
    def new_loss(self):
        self.losses += 1

    # Outputs the SoccerTeams season status information
    # Info is team's name, their wins-loss and their W/L Ratio
    # Based on W/L Ratio, return a string that determines off-season qualifications and gives team feedback
    def season_status(self):
        homeTeamRecord = self.wins / (self.wins + self.losses)
        print(f'{self.teamName} has a record of {self.wins}-{self.losses} and a W/L Ratio is {self.calc_win_loss_ratio()}')
        if homeTeamRecord >= 0.75:
            return "Qualified for the NCAA Women's Soccer Tournament"
        elif homeTeamRecord >= 0.5:
            return "You had a good season"
        else:
            return "Your team needs to practice!"

    # Calculate the SoccerTeam's W/L Ratio
    def calc_win_loss_ratio(self):
        if self.losses == 0:
            self.winLossRatio = 1.0
        else:
            self.winLossRatio = self.wins / (self.wins + self.losses)
        return round(self.winLossRatio,2)


team1 = SoccerTeam(teamName="BYU", wins=6, losses=2, gf=47, ga=4)
print(f'{team1.season_status()}')

