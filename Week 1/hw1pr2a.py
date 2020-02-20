# coding: utf-8
#
# hw1pr2a.py
#

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon: rock, paper, or scissors? ")
    comp = random.choice(['rock','paper','scissors'])
    print() #This is here to provide a space between the first question, and what the characters chose 

    print('The user (you)   chose', user) #prints what the user inputed
    print('The computer (I) chose', comp) #prints the random choice made by the computer
    print() #This provide another space between the choices and the end result

    if user == 'rock': #This runs if the user choses rock
        print('Ha! I really chose paper--I WIN!')

        print("Better luck next time...")
    if user == 'paper': #This runs if the user choses paper
        print("Ha! I really chose scissors--I WIN!")

        print("Better luck next time...")
    if user == 'scissors': #This runs if the user choses scissors
        print("Ha! I really chose rock--I WIN!")

        print("Better luck next time...")
    
        