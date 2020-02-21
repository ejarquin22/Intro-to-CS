# CS5, Lab2 part 2
# Filename: hw2pr2.py
# Name: 
# Problem description: First few functions!


def dbl(x):
    """Result: dbl returns twice its argument
       Argument x: a number (int or float)
       Spam is great, and dbl("spam") is better!
    """
    return 2*x

def sq(x):
    """Result: sq retuens the arguement time itself
        Arguement x: a number (int or float)
    """
    return x*x

def interp(low, hi, fraction):
    """Rsult: interp retuens the first arguemnt low, subraacted from the second
        arguemtn 'hi', multiplied by the third argument 'fraction', the subtracted by the first argument 'low'
        Arguement hi, low, fraction: a number (int or float)
    """
    return (((hi - low)  * fraction) + low)

def checkends(s):
    """Result: checkends returns a boolean (True or False) depending on whether the 
        first charachter in a string is the same as the last charachter in the sting
        Arguement s: string
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

def flipside(s):
    """Result: flipside returns the second half ot the string entered first, and returns the first half right after
        Arguement s: String
    """
    x = len(s)//2
    return s[x:] + s[0:x]