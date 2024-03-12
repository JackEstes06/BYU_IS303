# Jack Estes
# 3/12/24
# Dictionary Practice

listTeams = []
iNum = int(input("How many teams? "))

for team in range(0, iNum):
    dictTeam = {}
    sTeam = input("Enter team name: ")
    iWins = int(input("Enter # of wins: "))

    dictTeam["teamName"] = sTeam
    dictTeam["wins"] = iWins

    listTeams.append(dictTeam)

print(listTeams)

for dictionary in listTeams:
    print(dictionary)
