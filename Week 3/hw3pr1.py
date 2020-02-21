#
# hw3pr1.py
#
# Name:
#
# Turtle graphics and recursion
#

import time
from turtle import *
from random import *

def tri(n):
    shape('turtle')
    clr = choice(['darkgreen', 'red', 'blue'])
    color(clr)
    """Draws n 100-pixel sides of an equilateral triangle.
       Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return      # No sides to draw, so stop drawing
    else:
        dot(10, 'red')
        width(2*n+1)
        forward(100)
        left(120)
        tri(n-1)    # Recur to draw the rest of the sides!
        reset()

def spiral(initialLength, angle, multiplier):
    x = initialLength * multiplier
    """Spiral-drawing function.  Arguments:
       initialLength = the length of the first leg of the spiral
       angle = the angle, in degrees, turned after each spiral's leg
       multiplier = the fraction by which each leg of the spiral changes
    """
    if initialLength <= 1:          
        return      # No more to draw, so stop this call to spiral
    if initialLength >= 1000:
        return
    else:
        forward(initialLength) # You will want a call to forward here...
        left(angle) # You will want a turn here...
        spiral(x, angle, multiplier) # You will want to recur here! That is, make a new call to spiral...

def chai(size):
    """Our chai function!"""
    if (size < 5): 
        return
    else:
        forward(size)
        left(90)
        forward(size/2)
        right(90)
        chai(size/2)
        right(90)
        forward(size)
        left(90)
        chai(size/2)
        left(90)
        forward(size/2.0)
        right(90)
        backward(size)
        return

def svtree(trunklength, levels):
    c = choice(['brown', 'darkred', 'gold'])
    color(c)
    """svtree: draws a side-view tree
       trunklength = the length of the first line drawn ("the trunk")
       levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        width(5)
        forward(trunklength) # Draw the original trunk (1 line)
        left(15) # Turn a little bit to position the first subtree (1 line)
        svtree(trunklength/1.1, levels-1) # Recur! with both a smaller trunk and fewer levels (1 line)
        right(30) # Turn the other way to position the second subtree (1 line)
        svtree(trunklength/1.1, levels-1) # Recur again! (1 line)
        left(15)
        backward(trunklength) # Turn and go BACKWARDS (2 steps: 2 lines)
        return

def flakeside(sidelength, levels):
    x = sidelength/3
    if levels == 0:
        return forward(sidelength)
    else:
        flakeside(x, levels-1)
        right(60)
        flakeside(x, levels-1)
        left(120)
        flakeside(x, levels-1)
        right(60)
        flakeside(x, levels-1)
        return



def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
       sidelength: pixels in the largest-scale triangle side
       levels: the number of recursive levels in each side
    """
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    return