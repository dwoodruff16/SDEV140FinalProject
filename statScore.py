"""
File: statScore
Final Project
Code for the calculation of stat scores as listed int the D&D PHB
"""

from die import Die


class Statscore:

    def __init__(self):
        # creates 4 dice and a list to store their rolls and variables to store the total and the minimum
        self.die1 = Die() #first die
        self.die2 = Die() #second die
        self.die3 = Die() #third die
        self.die4 = Die() #fourth die
        self.rolls = [] #list of die rolls
        self.dieTotal = 0 #sum of all dice
        self.dieMin = 0 #value of lowest dice roll
        self.score = 0 #final score

    def rolldice(self):
        # rolls the dice 1 time and removes the lowest value then adds remaining dice together
        self.die1.roll()
        self.die2.roll()
        self.die3.roll()
        self.die4.roll()
        self.rolls = (self.die1.getValue(), self.die2.getValue(), self.die3.getValue(), self.die4.getValue())
        self.dieMin = min(self.rolls)
        self.dieTotal = sum(self.rolls)
        self.score = self.dieTotal - self.dieMin
        return self.score

