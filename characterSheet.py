"""
File: characterSheet
Final Project
Code to display the character sheet
"""
from breezypythongui import EasyFrame
from modCalculator import modCalc
from tkinter import PhotoImage
from tkinter.font import Font

class Sheet(EasyFrame):

    def __init__(self, name, race, pClass, strStat, dexStat, conStat, intStat, wisStat, chaStat):
        #initializes data for the character sheet
        EasyFrame.__init__(self, title = "Character Sheet")
        self.name = name #character name
        self.race = race # character race
        self.pClass = pClass #character class
        self.strStat = strStat #str score
        self.dexStat = dexStat #dex score
        self.conStat = conStat #con score
        self.intStat = intStat #int score
        self.wisStat = wisStat #wis score
        self.chaStat = chaStat #cha score

        #labels displayed in the sheet
        self.nameLabel = self.addLabel(text = self.name, row = 0, column = 0, sticky = "NW")
        self.rcLabel = self.addLabel(text = self.race + " " + self.pClass, row = 1, column = 0, sticky = "NW")
        self.scoreLabel = self.addLabel(text = "Score", row = 3, column = 1, sticky = "NSEW")
        self.modLabel = self.addLabel(text = "Modifier", row = 3, column = 2, sticky = "NSEW")
        self.strLabel = self.addLabel(text = "Str:", row = 4, column = 0, sticky = "NSEW")
        self.dexLabel = self.addLabel(text = "Dex:", row = 5, column = 0, sticky = "NSEW")
        self.conLabel = self.addLabel(text = "Con:", row = 6, column = 0, sticky = "NSEW")
        self.intLabel = self.addLabel(text = "Int:", row = 7, column = 0, sticky = "NSEW")
        self.wisLabel = self.addLabel(text = "Wis:", row = 8, column = 0, sticky = "NSEW")
        self.chaLabel = self.addLabel(text = "Cha:", row = 9, column = 0, sticky = "NSEW")
        self.strStatLabel = self.addLabel(text = self.strStat, row = 4, column = 1, sticky = "NSEW")
        self.dexStatLabel = self.addLabel(text = self.dexStat, row = 5, column = 1, sticky = "NSEW")
        self.conStatLabel = self.addLabel(text = self.conStat, row = 6, column = 1, sticky = "NSEW")
        self.intStatLabel = self.addLabel(text = self.intStat, row = 7, column = 1, sticky = "NSEW")
        self.wisStatLabel = self.addLabel(text = self.wisStat, row = 8, column = 1, sticky = "NSEW")
        self.chaStatLabel = self.addLabel(text = self.chaStat, row = 9, column = 1, sticky = "NSEW")
        self.strModLabel = self.addLabel(text = modCalc(self.strStat), row = 4, column = 2, sticky = "NSEW")
        self.dexModLabel = self.addLabel(text = modCalc(self.dexStat), row = 5, column = 2, sticky = "NSEW")
        self.conModLabel = self.addLabel(text = modCalc(self.conStat), row = 6, column = 2, sticky = "NSEW")
        self.intModLabel = self.addLabel(text = modCalc(self.intStat), row = 7, column = 2, sticky = "NSEW")
        self.wisModLabel = self.addLabel(text = modCalc(self.wisStat), row = 8, column = 2, sticky = "NSEW")
        self.chaModLabel = self.addLabel(text = modCalc(self.chaStat), row = 9, column = 2, sticky = "NSEW")
        self.classImage = self.addLabel(text = "Class Image", row = 4, column = 3, columnspan = 2, rowspan = 6, sticky = "NSEW")

        #selects which image to display based on the given class
        if self.pClass == "Fighter":
            self.imageClass = PhotoImage(file = "fighter class.gif")
            self.classImage["image"] = self.imageClass

        elif self.pClass == "Rogue":
            self.imageClass = PhotoImage(file = "rogue class.gif")
            self.classImage["image"] = self.imageClass

        elif self.pClass == "Wizard":
            self.imageClass = PhotoImage(file = "wizard class.gif")
            self.classImage["image"] = self.imageClass

# used to run the code when testing
#def main():
#    Sheet().mainloop()

#if __name__ == "__main__":
#    main()