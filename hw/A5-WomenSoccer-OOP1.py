class SoccerTeam:
    def __init__(self, teamName="", wins=0, losses=0, gf=0, ga=0):
        self.teamName = teamName
        self.wins = wins
        self.losses = losses
        self.goalsFor = gf
        self.goalsAgainst = ga
        self.winLossRatio = self.calc_win_loss_ratio()

    def newWin(self):
        self.wins += 1

    def newLoss(self):
        self.losses += 1

    def display_team_info(self):
        return f'{self.teamName} has a record of {self.wins}-{self.losses}'

    def calc_win_loss_ratio(self):
        if self.losses == 0:
            self.winLossRatio = 1.0
        else:
            self.winLossRatio = self.wins / (self.wins + self.losses)
        return self.winLossRatio


team1 = SoccerTeam(teamName="BYU", wins=5, losses=0, gf=47, ga=4)
print(f'{team1.display_team_info()} and a W/L Ratio is {team1.winLossRatio}')
