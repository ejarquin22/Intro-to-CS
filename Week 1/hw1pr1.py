# CS5 Gold/Black: Lab 1, Problem 1
# Filename: hw1pr1.py
# Name: Emanuel Jarquin
# Problem description: The four fours challenge!

from math import *

print("Zero is", 4+4-4-4)
print("One is", (4+4)/(4+4))
print("Two is", (4*4)/(4+4))
print("Three is", ((4*4)-4)/4)
print("Four is", (4-4)/4+4)
print("Five is", (4*4+4)/4)
print("Six is", (4+4+4)/sqrt(4))
print("Seven is", (4-4/4+4))
print("Eight is", 4+4+4-4)
print("Nine is", 4+4+(4/4))
print("Ten is", (4+4)+(4/(sqrt(4))))
print("Eleven is", (44/((sqrt(4))+sqrt(4))))
print("Twelve is", (4+4)+sqrt(4)+sqrt(4))
print("Fifteen is", 4/4+4*4)
print("Sixteen is", (4**4)/(4*4))
print("Seventeen is", 4/4+4*4)
print("Twenty is", (4*4)+sqrt(4)+sqrt(4))


def alex(x):
    if x == 3:
        return True
    else:
        return False

