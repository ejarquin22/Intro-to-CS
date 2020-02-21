# CS 5 Gold, hw3pr3
# filename: hw3pr3.py
# Name:
# problem description: List comprehensions



# this gives us functions like sin and cos...
from math import *



# two more functions (not in the math library above)

def dbl(x):
    """Doubler!  argument: x, a number"""
    return 2*x

def sq(x):
    """Squarer!  argument: x, a number"""
    return x**2



# examples for getting used to list comprehensions...

def lc_mult(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each multiplied by 2**
    """
    return [2*x for x in range(N)]

def lc_idiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       WARNING: this is INTEGER division...!
    """
    return [float(x//2) for x in range(N)]

def lc_fdiv(N):
    """This example accepts an integer N
       and returns a list of integers
       from 0 to N-1, **each divided by 2**
       NOTE: this is floating-point division...!
    """
    return [x/2 for x in range(N)]

assert lc_mult(4) == [0, 2, 4, 6]
assert lc_idiv(4) == [0, 0, 1, 1]
assert lc_fdiv(4) == [0.0, 0.5, 1.0, 1.5]

# Here is where your functions start for the lab:

# Step 1, part 1
def unitfracs(N):
    '''unitfracs returns a list that divides the list position of x
        by N. 
        argument N: a number ( int or float)
    '''
    return [x/N for x in range(N)]

assert unitfracs(2) == [0.0, 0.5]
assert unitfracs(4) == [0.0, 0.25, 0.5, 0.75]
assert unitfracs(5) == [0.0, 0.2, 0.4, 0.6, 0.8]

def scaledfracs(low, hi, N):
    '''scaledfracs returns a list containing
        floats going from low to hi, adding the product
        of hi minus low times the x positions of unitfracs.
        argument low: a number (int or float)
        argument hi: a number (int or float)
        argument N: a number (int or float)
    '''
    return [low + (hi-low)*(x) for x in unitfracs(N)]

assert scaledfracs(10, 30, 5) == [10.0, 14.0, 18.0, 22.0, 26.0]
assert scaledfracs(41, 43, 8) == [41.0, 41.25, 41.5, 41.75, 42.0, 42.25, 42.5, 42.75]
assert scaledfracs(0, 10, 4) == [0.0, 2.5, 5.0, 7.5]

def sqfracs(low, hi, N):
    '''sqfracs returns a list that squared each value in the
        list from scaledfracs
        argument low: a number (int or float)
        argument hi: a number (int or float)
        argument N: a number (int or float)
    '''
    return [x**2 for x in scaledfracs(low, hi, N)]

assert sqfracs(4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert sqfracs(0, 10, 5) == [0.0, 4.0, 16.0, 36.0, 64.0]

def f_of_fracs(f, low, hi, N):
    '''f_of_fracts runs the list poistions in scaledfracts 
        through another function f.
        argument f: a function 
        argument low: a number (int or float)
        argument hi: a number (int or float)
        argument N: a number (int or float)
    '''
    return [f(x) for x in scaledfracs(low, hi, N)]

assert f_of_fracs(dbl, 10, 20, 5) == [20.0, 24.0, 28.0, 32.0, 36.0]
assert f_of_fracs(sq, 4, 10, 6) == [16.0, 25.0, 36.0, 49.0, 64.0, 81.0]
assert f_of_fracs(sin, 0, pi, 2) == [0.0, 1.0]

def integrate(f, low, hi, N):
    """Integrate returns an estimate of the definite integral
       of the function f (the first argument)
       with lower limit low (the second argument)
       and upper limit hi (the third argument)
       where N steps are taken (the fourth argument)

       integrate simply returns the sum of the areas of rectangles
       under f, drawn at the left endpoints of N uniform steps
       from low to hi
    """
    return sum(f_of_fracs( f, low, hi, N)) * (hi/N)
assert integrate(dbl, 0, 10, 4) == 75
assert integrate(sq, 0, 10, 4) == 2.5 * sum([0, 2.5*2.5, 5*5, 7.5*7.5])

def c(x):
    """c is a semicircular function of radius two"""
    return (4 - x**2)**0.5

'''Question 1:
    Integrate will always underestimate the correct answer becuase there are an infinite amount of values that 
    python will have to go thru to reach the correct answer.

    follow up: right-hand enpoint rectangles

    Question 2:
    As N goes to infinity, the vlaue of this integral goes to zero. This is 
    because function c is rasing to the .5 power. as the number gets larger,
    the output becomes clsoer to zero.

'''