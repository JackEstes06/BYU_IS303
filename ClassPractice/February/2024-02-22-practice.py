# Jack Estes
# BYU IS303 Section 3
# Class Practice

class Coach:
    def __init__(self, name="", wins=0, losses=0):
        self.name = name
        self.career_wins = wins
        self.career_losses = losses

    def displayCoachInfo(self):
        return f'{self.name} with a {self.career_wins}-{self.career_losses} career record'


class SoccerTeam:
    def __init__(self, name="", wins=0, losses=0, coach=Coach()):
        self.teamName = name
        self.wins = wins
        self.losses = losses
        self.win_loss_pct = self.calc_win_loss_ratio()
        self.coach = coach

    # Display team info
    def displayTeamInfo(self):
        return f'{self.teamName} has a record of {self.wins}-{self.losses} coached by {self.coach.displayCoachInfo()}'

    # Add a win to SoccerTeam.wins
    def new_win(self):
        self.wins += 1

    # Add a loss to SoccerTeam.losses
    def new_loss(self):
        self.losses += 1

    # Calculate the SoccerTeam's W/L Ratio
    def calc_win_loss_ratio(self):
        if self.losses == 0:
            self.winLossRatio = 1.0
        else:
            self.winLossRatio = self.wins / (self.wins + self.losses)
        return round(self.winLossRatio,2)


coach1 = Coach("Mr. T", 100, 0)
team1 = SoccerTeam("BYU", 10, 0, coach1)
print(team1.displayTeamInfo())

