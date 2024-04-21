# Jack Estes
# IS303 - Section 3
# Final Exam - Gym member data processing

import random
import pandas as pd


# Standard gym member
class StandardMember:
    def __init__(self, name="", gender="", numDaysMember=0, numGymVisits=0, favWorkout="", membershipType=""):
        self.name = name
        self.gender = gender
        self.numDaysMember = numDaysMember
        self.numGymVisits = numGymVisits
        self.favWorkout = favWorkout
        self.membershipType = membershipType

    # Prints out a recommended action based on how often they’ve gone to the gym
    def recommendedAction(self, shouldPrint=True):
        # Set recommendation based on visitRatio calculated
        visitRatio = self.numGymVisits / self.numDaysMember
        if visitRatio > .5:
            recommendedAction = f"Recommended Action for {self.name} ({self.gender}): Keep up the routine!"
        elif visitRatio > .3:
            recommendedAction = f"Recommended Action for {self.name} ({self.gender}): Slightly increase visits."
        else:
            recommendedAction = f"Recommended Action for {self.name} ({self.gender}): Increase your frequency."

        # Allows inherited classes to add onto the print statement if wanted, otherwise prints the recommendation
        if shouldPrint:
            print(recommendedAction)
        else:
            return recommendedAction

    def memberInfo(self):
        print(
            f"{self.name} is a {self.gender} that has been a member for {self.numDaysMember} days and has visited "
            f"{self.numGymVisits} times."
            f"\nTheir favorite workout is {self.favWorkout} and they are a {self.membershipType} member.\n")


# Premium gym member - inherits from StandardMember & also has a potential trainer that is defaulted to None
class PremiumMember(StandardMember):
    def __init__(self, name="", gender="", numDaysMember=0, numGymVisits=0, favWorkout="", membershipType="",
                 trainer=None):
        super().__init__(
            name=name,
            gender=gender,
            numDaysMember=numDaysMember,
            numGymVisits=numGymVisits,
            favWorkout=favWorkout,
            membershipType=membershipType,
        )
        self.trainer = trainer

    # Prints out a recommended action based on how often they’ve gone to the gym, and how their trainer feels about it
    def recommendedAction(self, shouldPrint=True):
        visitRatio = self.numGymVisits / self.numDaysMember
        recommendedAction = super().recommendedAction(shouldPrint=False)
        if visitRatio > .5:
            recommendedAction += f"{self.trainer.name} ({self.trainer.gender}) is proud!"
        elif visitRatio > .3:
            recommendedAction += f"{self.trainer.name} ({self.trainer.gender}) is encouraging you!"
        else:
            recommendedAction += f"{self.trainer.name} ({self.trainer.gender}) still believes in you!"

        # Allows inherited classes to add onto the print statement if wanted by returning the recommendation string,
        # otherwise prints the recommendation
        if shouldPrint:
            print(recommendedAction)
        else:
            return recommendedAction

    def memberInfo(self):
        print(
            f"{self.name} is a {self.gender} that has been a member for {self.numDaysMember} days and has visited "
            f"{self.numGymVisits} times."
            f"\nTheir favorite workout is {self.favWorkout} and they are a {self.membershipType} member and they have "
            f"{self.trainer.trainerInfo()} as a trainer.\n")


# Trainer class for gym members
class Trainer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def trainerInfo(self):
        print(f"{self.name} is a {self.gender}")


# Here is where the logical flow of the program occurs.
# Data from 2 spreadsheets are pulled in, parsed, and utilized.
membersDF = pd.read_excel('gym_members.xlsx')
trainersDF = pd.read_excel('gym_trainers.xlsx')
print(membersDF)
print()
print(trainersDF)

# Lists that store all gym members and trainers
gymMembers = []
gymTrainers = []

# Add all members from the members dataframe to the gymMembers list as either standard or premium members
for index, row in membersDF.iterrows():
    # Determine if member is premium or not -> all members not premium are defaulted to standard
    if row["membership_type"] == "Premium":
        gymMembers.append(PremiumMember(
            name=row["name"],
            gender=row["gender"],
            numDaysMember=row["num_days_member"],
            numGymVisits=row["num_gym_visits"],
            favWorkout=row["favorite_workout"],
            membershipType=row["membership_type"],
        ))
    else:
        gymMembers.append(StandardMember(
            name=row["name"],
            gender=row["gender"],
            numDaysMember=row["num_days_member"],
            numGymVisits=row["num_gym_visits"],
            favWorkout=row["favorite_workout"],
            membershipType=row["membership_type"],
        ))

    # Get the most recently added members info in the terminal output for testing
    gymMembers[-1].memberInfo()

# Add all trainers from the trainers dataframe to the gymTrainers list
for index, row in trainersDF.iterrows():
    gymTrainers.append(Trainer(
        name=row["Name"],
        gender=row["Gender"],
    ))

# Give a recommended action to each gym member
# Also randomly assign all PremiumMembers a trainer
for member in gymMembers:
    member.recommendedAction()
    randomTrainer = random.randint(0, 2)
