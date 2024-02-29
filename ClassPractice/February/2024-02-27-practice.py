class SoccerTeam():
    def __init__(self):
        self.team_name = ""
        self.wins = 0
        self.losses = 0
        self.win_loss_pct = 0.0
        self.coach = Coach("Default Greg")

    def calcWinLoss(self):
        self.win_loss_pct = self.wins / (self.wins + self.losses)

    def displayInfo(self):
        return self.team_name + " has " + str(self.wins) + " wins"

    def newWin(self):
        self.wins += 1
        self.coach.career_wins += 1

    def newLoss(self):
        self.losses += 1
        self.coach.career_losses += 1


class Person():
    def __init__(self, name):
        self.name = name


class Coach(Person):
    def __init__(self, name):
        super().__init__(name)
        self.career_wins = 0
        self.career_losses = 0

    def displayInfo(self):
        return self.name + " has " + str(self.career_wins) + " wins"


oTeam = SoccerTeam()
oTeam.team_name = "BYU"
oCoach = Coach("Jennifer Rockwood")
oTeam.coach = oCoach
for iCount in range(0, 5):
    oTeam.newWin()
oTeam.newLoss()
oTeam.calcWinLoss()
print(oTeam.displayInfo())
print(oTeam.coach.displayInfo())
