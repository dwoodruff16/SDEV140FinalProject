"""
File: characterCreator
Final Project
Code to create a D&D character
"""
from breezypythongui import EasyFrame
from statScore import Statscore
from tkinter import PhotoImage
from tkinter.font import Font
from raceSelector import Raceselector
from characterSheet import Sheet
from tkinter import *

class StatAssign(EasyFrame):

    def __init__(self):
        #creates buttons and fields for the user to interact with to help determine scores, race, and class
        EasyFrame.__init__(self, title = "Stat Assignment")
        self.titleImage = self.addLabel(text = "Character Creation", row = 0, column = 0, columnspan = 6, sticky = "NSEW")
        self.nameLabel = self.addLabel(text = "Name:", row = 1, column = 0, sticky = "NSEW")
        self.nameEntry = self.addTextField(text = "", row = 1, column = 1, width = 25)
        self.strLabel = self.addLabel(text = "Str", row = 2, column = 0, sticky = "NSEW")
        self.strEntry = self.addIntegerField(value = 0, row = 3, column = 0, width = 20)
        self.strCalcbutton = self.addButton(text = "Calculate Str", row = 4, column = 0, command = self.strCalc)
        self.dexLabel = self.addLabel(text = "Dex", row = 2, column = 1, sticky = "NSEW")
        self.dexEntry = self.addIntegerField(value = 0, row = 3, column = 1, width = 20)
        self.dexCalcbutton = self.addButton(text = "Calculate Dex", row = 4, column = 1, command = self.dexCalc)
        self.conLabel = self.addLabel(text = "Con", row = 2, column = 2, sticky = "NSEW")
        self.conEntry = self.addIntegerField(value = 0, row = 3, column = 2, width = 20)
        self.conCalcbutton = self.addButton(text = "Calculate Con", row = 4, column = 2, command = self.conCalc)
        self.intLabel = self.addLabel(text = "Int", row = 2, column = 3, sticky = "NSEW")
        self.intEntry = self.addIntegerField(value = 0, row = 3, column = 3, width = 20)
        self.intCalcbutton = self.addButton(text = "Calculate Int", row = 4, column = 3, command = self.intCalc)
        self.wisLabel = self.addLabel(text = "Wis", row = 2, column = 4, sticky = "NSEW")
        self.wisEntry = self.addIntegerField(value = 0, row = 3, column = 4, width = 20)
        self.wisCalcbutton = self.addButton(text = "Calculate Wis", row = 4, column = 4, command = self.wisCalc)
        self.chaLabel = self.addLabel(text = "Cha", row = 2, column = 5, sticky = "NSEW")
        self.chaEntry = self.addIntegerField(value = 0, row = 3, column = 5, width = 20)
        self.chaCalcbutton = self.addButton(text = "Calculate Cha", row = 4, column = 5, command = self.chaCalc)
        self.lockStatbutton = self.addButton(text = "Lock Stats", row = 5, column = 2, columnspan = 2, command = self.lockStat)
        self.failLabel = self.addLabel(text = "", row = 6, column = 2, columnspan = 2, sticky = "NSEW")
        self.raceLabel = self.addLabel(text = "Race", row = 7, column = 0, sticky = "NSEW")
        self.humanButton = self.addButton(text = "Human", row = 8, column = 0, command = self.raceHuman, state = "disabled")
        self.elfButton = self.addButton(text = "Elf", row = 8, column = 1, command = self.raceElf, state = "disabled")
        self.dwarfButton = self.addButton(text = "Dwarf", row = 8, column = 2, command = self.raceDwarf, state = "disabled")
        self.halforcButton = self.addButton(text = "Half-Orc", row = 8, column = 3, command = self.raceHalforc, state = "disabled")
        self.subLabel = self.addLabel(text = "Subrace", row = 9, column = 0, sticky = "NSEW")
        self.highElfButton = self.addButton(text = "High", row = 10, column = 0, command = self.subHighElf, state = "disabled")
        self.woodElfButton = self.addButton(text = "Wood", row = 10, column = 1, command = self.subWoodElf, state = "disabled")
        self.darkElfButton = self.addButton(text = "Dark", row = 10, column = 2, command = self.subDarkElf, state = "disabled")
        self.hillDwarfButton = self.addButton(text = "Hill", row = 11, column = 0, command = self.subHillDwarf, state = "disabled")
        self.mountDwarfButton = self.addButton(text = "Mountain", row = 11, column = 1, command = self.subMountDwarf, state = "disabled")
        self.noSubLabel = self.addLabel(text = "", row = 12, column = 0, columnspan = 2, sticky = "NSEW")
        self.pClassLabel = self.addLabel(text = "Class", row = 13, column = 0, sticky = "NSEW")
        self.fighterButton = self.addButton(text = "Fighter", row = 14, column = 0, command = self.fighter, state = "disabled")
        self.rogueButton = self.addButton(text = "Rogue", row = 14, column = 1, command = self.rogue, state = "disabled")
        self.wizardButton = self.addButton(text = "Wizard", row = 14, column = 2, command = self.wizard, state = "disabled")
        self.generateButton = self.addButton(text = "Generate Character", row = 15, column = 2, columnspan = 2, command = self.generate, state = "disabled")
        self.noNameLabel = self.addLabel(text = "", row = 16, column = 2, columnspan = 2, sticky = "NSEW")

        #adds the title image
        self.imageTitle = PhotoImage(file="character creation.gif")
        self.titleImage["image"] = self.imageTitle

        #initialized data to be passed into later functions
        self.pClass = "" #character class
        self.race = "race" #character race

    def strCalc(self):
        #calculates and sets a random str score
        score = Statscore()
        self.strEntry.setNumber(score.rolldice())

    def dexCalc(self):
        #calculates and sets a random dex score
        score = Statscore()
        self.dexEntry.setNumber(score.rolldice())

    def conCalc(self):
        #calculates and sets a random con score
        score = Statscore()
        self.conEntry.setNumber(score.rolldice())

    def intCalc(self):
        #calculates and sets a random int score
        score = Statscore()
        self.intEntry.setNumber(score.rolldice())

    def wisCalc(self):
        #calculates and sets a random wis score
        score = Statscore()
        self.wisEntry.setNumber(score.rolldice())

    def chaCalc(self):
        #calculates and sets a random cha score
        score = Statscore()
        self.chaEntry.setNumber(score.rolldice())

    def lockStat(self):
        #locks final scores in after checking to see if they are acceptable (between 3 and 18)

        #recieves final scores
        strScore = self.strEntry.getNumber()
        dexScore = self.dexEntry.getNumber()
        conScore = self.conEntry.getNumber()
        intScore = self.intEntry.getNumber()
        wisScore = self.wisEntry.getNumber()
        chaScore = self.chaEntry.getNumber()

        #checks for scores to be between 3 and 18
        if strScore >= 3 and strScore <= 18 and dexScore >= 3 and dexScore <= 18 and conScore >= 3 and conScore <= 18 and intScore >= 3 and intScore <= 18 and wisScore >= 3 and wisScore <= 18 and chaScore >= 3 and chaScore <= 18:
            self.strCalcbutton["state"] = "disabled"
            self.strEntry["state"] = "disabled"
            self.dexCalcbutton["state"] = "disabled"
            self.dexEntry["state"] = "disabled"
            self.conCalcbutton["state"] = "disabled"
            self.conEntry["state"] = "disabled"
            self.intCalcbutton["state"] = "disabled"
            self.intEntry["state"] = "disabled"
            self.wisCalcbutton["state"] = "disabled"
            self.wisEntry["state"] = "disabled"
            self.chaCalcbutton["state"] = "disabled"
            self.chaEntry["state"] = "disabled"
            # marks data as in spec
            OOS = False
        else:
            #marks data as out of spec or OOS
            OOS = True


        if OOS == True:
            #runs if data is out of spec letting user know data needs to be changed
            self.failLabel["text"] = "Stat Scores Out of Spec"
        else:
            #runs if data is in spec, removing the user warning and locking final score then unlocks race buttons
            self.lockStatbutton["state"] = "disabled"
            self.failLabel["text"] = ""
            self.humanButton["state"] = "normal"
            self.elfButton["state"] = "normal"
            self.dwarfButton["state"] = "normal"
            self.halforcButton["state"] = "normal"

    def raceHuman(self):
        #raises the stat scores relevant to a human
        statInc = Raceselector("Human")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])

        #locks race buttons informs the user humans do not have subraces then unlocks the class button
        self.humanButton["state"] = "disabled"
        self.elfButton["state"] = "disabled"
        self.dwarfButton["state"] = "disabled"
        self.halforcButton["state"] = "disabled"
        self.noSubLabel["text"] = "Humans do not have subraces"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"
        #sets race to human
        self.race = "Human"

    def raceElf(self):
        #raises the stat scores relevant to an elf and unlocks relevant subrace buttons
        statInc = Raceselector("Elf")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.humanButton["state"] = "disabled"
        self.elfButton["state"] = "disabled"
        self.dwarfButton["state"] = "disabled"
        self.halforcButton["state"] = "disabled"
        self.highElfButton["state"] = "normal"
        self.woodElfButton["state"] = "normal"
        self.darkElfButton["state"] = "normal"

    def raceDwarf(self):
        #raises the stat scores relevant to a dwarf and unlocks relevant subrace buttons
        statInc = Raceselector("Dwarf")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.humanButton["state"] = "disabled"
        self.elfButton["state"] = "disabled"
        self.dwarfButton["state"] = "disabled"
        self.halforcButton["state"] = "disabled"
        self.hillDwarfButton["state"] = "normal"
        self.mountDwarfButton["state"] = "normal"

    def raceHalforc(self):
        #raises the stat scores relevant to a half-orc, informs the user that Half-Orcs do not have a sub race, and unlocks class buttons
        statInc = Raceselector("Half-Orc")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.humanButton["state"] = "disabled"
        self.elfButton["state"] = "disabled"
        self.dwarfButton["state"] = "disabled"
        self.halforcButton["state"] = "disabled"
        self.noSubLabel["text"] = "Half-Orcs do not have subraces"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to Half-Orc
        self.race = "Half-Orc"

    def subHighElf(self):
        # raises the stat scores relevant to a high elf and unlocks class buttons
        statInc = Raceselector("High")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.highElfButton["state"] = "disabled"
        self.woodElfButton["state"] = "disabled"
        self.darkElfButton["state"] = "disabled"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to high elf
        self.race = "High Elf"

    def subWoodElf(self):
        # raises the stat scores relevant to a wood elf and unlocks class buttons
        statInc = Raceselector("Wood")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.highElfButton["state"] = "disabled"
        self.woodElfButton["state"] = "disabled"
        self.darkElfButton["state"] = "disabled"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to wood elf
        self.race = "Wood Elf"

    def subDarkElf(self):
        # raises the stat scores relevant to a Dark elf and unlocks class buttons
        statInc = Raceselector("Dark")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.highElfButton["state"] = "disabled"
        self.woodElfButton["state"] = "disabled"
        self.darkElfButton["state"] = "disabled"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to dark elf
        self.race = "Dark Elf"

    def subHillDwarf(self):
        # raises the stat scores relevant to a Hill Dwarf and unlocks class buttons
        statInc = Raceselector("Hill")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.hillDwarfButton["state"] = "disabled"
        self.mountDwarfButton["state"] = "disabled"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to hill dwarf
        self.race = "Hill Dwarf"

    def subMountDwarf(self):
        # raises the stat scores relevant to a mountain Dwarf and unlocks class buttons
        statInc = Raceselector("Mount")
        stats = statInc.raceStat()
        self.strEntry.setNumber(self.strEntry.getNumber() + stats[0])
        self.dexEntry.setNumber(self.dexEntry.getNumber() + stats[1])
        self.conEntry.setNumber(self.conEntry.getNumber() + stats[2])
        self.intEntry.setNumber(self.intEntry.getNumber() + stats[3])
        self.wisEntry.setNumber(self.wisEntry.getNumber() + stats[4])
        self.chaEntry.setNumber(self.chaEntry.getNumber() + stats[5])
        self.hillDwarfButton["state"] = "disabled"
        self.mountDwarfButton["state"] = "disabled"
        self.fighterButton["state"] = "normal"
        self.rogueButton["state"] = "normal"
        self.wizardButton["state"] = "normal"

        #sets race to mountain dwarf
        self.race = "Mountain Dwarf"

    def fighter(self):
        #sets fighter class
        self.pClass = "Fighter"
        self.fighterButton["state"] = "disabled"
        self.rogueButton["state"] = "disabled"
        self.wizardButton["state"] = "disabled"
        self.generateButton["state"] = "normal"

    def rogue(self):
        #sets rogue class
        self.pClass = "Rogue"
        self.fighterButton["state"] = "disabled"
        self.rogueButton["state"] = "disabled"
        self.wizardButton["state"] = "disabled"
        self.generateButton["state"] = "normal"

    def wizard(self):
        #sets wizard class
        self.pClass = "Wizard"
        self.fighterButton["state"] = "disabled"
        self.rogueButton["state"] = "disabled"
        self.wizardButton["state"] = "disabled"
        self.generateButton["state"] = "normal"

    def generate(self):
        #generates character sheet

        #recieves character name from the creator
        name = self.nameEntry.getText()

        #will not move on unless the character has a name (entry field is not empty)
        if name == "":
            #lets the user know to name their character
            self.noNameLabel["text"] = "Remember to Name Your Character"

        else:
            self.noNameLabel["text"] = ""
            #creats character sheet
            Sheet(name, self.race, self.pClass, self.strEntry.getNumber(), self.dexEntry.getNumber(), self.conEntry.getNumber(), self.intEntry.getNumber(), self.wisEntry.getNumber(), self.chaEntry.getNumber()).mainloop()


def main():
    StatAssign().mainloop()

if __name__ == "__main__":
    main()