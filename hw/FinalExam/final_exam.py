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
    def recommendedAction(self):
        # TODO implement
        pass
    
    
# Premium gym member - inherits from StandardMember & also has a potential trainer that is defaulted to None
class PremiumMember(StandardMember):
    def __init__(self, name="", gender="", numDaysMember=0, numGymVisits=0, favWorkout="", membershipType="", trainer=None):
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
    def recommendedAction(self):
        # TODO implement
        pass
    
    
# Trainer class for gym members
class Trainer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
