# CS5 Gold, hw5pr1
# Filename: hw5pr1.py
# Name: 
# Problem description: Binary <-> decimal conversions

def isOdd(n):
    '''isOdd take a number n and returns a boolean for if n is odd or not.
        argument n: number (int or float)
    '''
    if n % 2 != 0: 
        return True
    else:
        return False

assert isOdd(42) == False
assert isOdd(43) == True

def numToBinary(N):
    """numToBinary takes a number N in decimal form and converts it 
        into binary form.
        argument N: a number (int)
    """
    if N == 0:
        return ''
    elif N % 2 == 1:
        return numToBinary(N//2) + '1'
    else:
        return numToBinary(N//2) + '0'

assert numToBinary(0) == ''
assert numToBinary(42) == '101010'

def binaryToNum(S):
    '''binaryToNum takes a string S that represents a binary number
        and converts it to a decimal number
        argumetn S: string
    '''
    if S == '':
        return 0

    # if the last digit is a '1'...
    elif S[-1] ==  '1':
        
        return (binaryToNum(S[0:-1])  << 1 ) + 1 
        
    
    else: # last digit must be '0'
       
        return (binaryToNum(S[0:-1])  << 1) + 0 

assert binaryToNum('') == 0
assert binaryToNum('101010') == 42

def increment(S):
    if S == '11111111':
        return '00000000'
    else: 
        x = binaryToNum(S) + 1
        y = numToBinary(x) 
        z = 8 - len(y)  
        return '0' * z + y

def count(S, n):
    if n == 0: 
        print(S)
    else: 
        print(S) 
        S = increment(S)
        return count(S, n-1)

         
    