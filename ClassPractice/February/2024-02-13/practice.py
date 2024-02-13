# Jack Estes
# BYU IS303 Section 3
# Object-Oriented Programming continued

class SoccerTeam:
    # Constructor
    def __init__(self):
        self.teamName = ""
        self.numWins = 0
        self.numLosses = 0
        self.winLossRatio = 0.0

    def display_team_info(self):
        return f'{self.teamName} has a record of {self.numWins}-{self.numLosses}'

    def calc_win_loss_ratio(self):
        if self.numLosses == 0:
            self.winLossRatio = 1.0
        else:
            self.winLossRatio = self.numWins / (self.numWins + self.numLosses)
        return self.winLossRatio


sTeam1 = SoccerTeam()
sTeam1.teamName = "BYU"
sTeam1Info = sTeam1.display_team_info()
print(f'{sTeam1Info}')
sTeam1WL = sTeam1.calc_win_loss_ratio()
print(f'{sTeam1.teamName} has a W-L ratio of {sTeam1WL}')

sTeam2 = SoccerTeam()
sTeam2.teamName = "UVU"
