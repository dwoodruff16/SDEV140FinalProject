"""
File: raceSelector
Final Project
Code for the score changes after selection of a character's race and subrace
"""


class Raceselector:

    def __init__(self, race):
        #initialized data and data recieved from the character creator
        self.race = race #race
        self.strStatgain = 0 #str stat gain
        self.dexStatgain = 0 #dex stat gain
        self.conStatgain = 0 #con Stat gain
        self.intStatgain = 0 #int stat gain
        self.wisStatgain = 0 #wis stat gain
        self.chaStatgain = 0 #cha stat gain
        self.stat = [self.strStatgain, self.dexStatgain, self.conStatgain, self.intStatgain, self.wisStatgain, self.chaStatgain] #list of all stat gains

    def raceStat(self):
        #sets modifier changes for each race and subrace
        if self.race == "Human":
            self.strStatgain = 1
            self.dexStatgain = 1
            self.conStatgain = 1
            self.intStatgain = 1
            self.wisStatgain = 1
            self.chaStatgain = 1

        elif self.race == "Elf":
            self.dexStatgain = 2

        elif self.race == "Dwarf":
            self.conStatgain = 2

        elif self.race == "Half-Orc":
            self.strStatgain = 2
            self.conStatgain = 1

        #the if else staments below this comment apply to sub races
        elif self.race == "High":
            self.intStatgain = 1

        elif self.race == "Wood":
            self.wisStatgain = 1

        elif self.race == "Dark":
            self.chaStatgain = 1

        elif self.race == "Hill":
            self.wisStatgain = 1

        elif self.race == "Mount":
            self.strStatgain = 2

        #list of stat changes
        self.stat = [self.strStatgain, self.dexStatgain, self.conStatgain, self.intStatgain, self.wisStatgain, self.chaStatgain]

        #returns stat changes to the character creator
        return self.stat
