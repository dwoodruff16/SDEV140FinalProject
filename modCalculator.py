"""
File: statScore
Final Project
Code for the calculation of a stat score to a stat modifier
"""
import math

def modCalc(score):
    #calculates the modifier based off of the received score
    mod = math.floor((score - 10) / 2)
    #returns the modifier
    return mod