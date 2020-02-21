# CS5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name:
# Problem description: Sleepwalking student

import random 
from random import *

def rs():
    """rs chooses a random step and returns it.
       note that a call to rs() requires parentheses
       arguments: none at all!
    """
    return choice([-1, 1])

def rwpos(start, nsteps):
    '''rwpos takes in the starting position and and the amount of steps
        and returns the the new poistion as many times as it is told.
        argument start: number (int or float)
        argument nsteps: number (int or float) 
    '''
    print('start is', + start)
    if nsteps == 0:
        return start
    else:
        start = start + rs()
        return rwpos(start, nsteps-1)
    
def rwsteps(start, low, hi):
    '''rwsteps will return a print line shwoing the position of the 
        sleep walker. The function will end when the starting poistion is equal to
        or less than the low, or is equal to or greater than the hi position.
        Argument start: number (int or float)
        Argument low: number (int or float)
        Argument hi: number (int or float)
    '''
    print('[' + '_' * start + '-.-' + '_' * start + ']')
    if start <= low or start >= hi:
        return 0
    else:
        newstart = start + rs()
        rest_of_steps = rwsteps(newstart, low, hi)
        return 1 + rest_of_steps

def rwposPlain(start, nsteps):
    '''rwposPlain will return the only the final position of the sleep walker.
        argument start: number (int or float)
        argument nsteps: number (int or float)
    '''
    if nsteps == 0:
        return start
    else:
        start = start + rs()
        return rwposPlain(start, nsteps-1)
    
def ave_signed_displacement(numtrials):
    '''ave_signed_displacement returns the average sign displavement
        of the sleepwalker.
        argument numtrial: number (int or float)
    '''
    LC = [rwposPlain(0, 100) for x in range(numtrials)]
    return (sum(LC)/len(LC))

def ave_squared_displacement(numtrials):
    '''ave_squared_displacement returns the average squared
        displacement of the sleepwalker
        arguemnt numtrials: numebr (int or float)
    '''
    LC = [(rwposPlain(0,100)**2) for x in range(numtrials)]
    return (sum(LC)/len(LC))

"""
     To compute the average signed displacement for
     a random walker after 100 random steps, I created a list comprehension
     called LC. In that list comprehension, I am calling for rhe first 100 positions (steps)
     using the call rwposPlain(0,100). The list comprehension will run for the given amount of times
     and in the end will return the sum of all the step-values, and divide it by the length of 
     the list comprehension. This will give us the average value.

        In: ave_signed_dispacelent(3)
        Out: 3.3333333

     To compute the average squared displacement for a 
     random walker, I did the same thing as I did for the average signed displacement
     except I squared every call for rwposPlain(0,100). 

        In: ave_squared_displacement(5)
        Out: 62.4
"""