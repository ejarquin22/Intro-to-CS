# coding: utf-8
#
# hw1pr2b.py
#

""" 
Title for your adventure:   The Quest.

Notes on how to "win" or "lose" this adventure:
  To win, choose the table.
  To lose, choose the door.

"""

import time

def adventure():
    """ this function runs one session of interactive fiction
        Well, it's "fiction," depending on the pill color chosen...
        arguments: no arguments (prompted text doesn't count as an argument)
        results: no results     (printing doesn't count as a result)
    """
    delay = 1.0          # change to 0.0 for testing or speed runs,
                         # ..larger for dramatic effect!

    username = input("Oui, mate. What's your name? ")

    print()
    print("That's crazy,", username, "is also my name!")
    print("But alright,", username, " welcome to Chilis!")
    print("Ill be your server today.")
    print()

    drink = input("What would you like to drink? We have sprite, coke, and water available. \nIf you want anything else, ill go check if we have it. ")
    if drink == "sprite":
        print("That is digusting, but as you wish.")
    elif drink == "coke":
        print("I guess..")
    elif drink == "water":
        print("A proper choice for a proper lad.")
    else:
        print("Ok, ill go check in the back if we have any...")
        time.sleep(delay)
        print("You're in luck, we just so happen to have", drink, "today!")
    print()

    food = input("Okay, Are you ready to eat? [yes/no] ")
    if food == "yes":
        print("Great!")
    elif food == "no":
        print("Too bad. You're out of time.")
    print()

    order = input("So, what'll you have? ")
    if order == "meat":
        print("big protien guy... my kinda guy.")
    elif order == "beans":
        print("I could tell you were a beans kinda guy before you even say down.")
    else:
        print(order, "? I guess..." )
    print()


    print("Okay.", username, "Here is your food.")
    

    choice = input("Would you like to leave a review of my service ability? ")
    if choice == "yes":
        print("Okay, Ill bring you a survey along with your check.")
    else:
        print("Too bad, you're getting a survey anyways.")
    print()

    print("Here's the survey.")
    
    question = input("Please re-enter your name to sign it. ")
    if question == username:
        print("Thanks for coming!")
    print("Bye!")