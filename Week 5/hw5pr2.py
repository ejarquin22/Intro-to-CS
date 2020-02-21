def numToBaseB(N, B):
    '''numToBase takes a number N and returns a string with N converted to 
        base B.
        Argument  N: a number (int)
        Argument  B: a number (int)
    '''
    if N == 0:
        return ''
    else:
        return numToBaseB(N//B, B) + str(N%B)

assert numToBaseB(0, 4) == ''
assert numToBaseB(42, 5) == '132'


def baseBToNum(S, B):
    '''baseBToNum will do the opposite of what numToBaseB did.
       Instead of taking a number N, it till take a string, and intead of 
       returning a string, it will reutn a number.
       argument S: string
       argument B: number (int)  
    '''
    if S == '':
        return 0
    else:
        return B*baseBToNum(S[:-1], B) + int(S[-1])

assert baseBToNum('1474462', 8) == 424242
assert baseBToNum('5733', 9) == 4242


def baseToBase(B1, B2, s_in_B1):
    '''baseToBase will take a string in B1 and return the string
       back in B2.
       argument B1: a number (int)
       argument B2: a number (int)
       argument s_in_B1: a string
    '''
    decimal = baseBToNum(s_in_B1, B1) 
    return numToBaseB(decimal, B2)

assert baseToBase(2, 4, '101010') == '222'
assert baseToBase(2, 5, '1001001010') == '4321'


def add(S, T):
    x = baseToBase(2, 10, S) #coverts string S from base 2 to 10
    y = baseToBase(2, 10, T) #same as above but for string T
    num1 = baseBToNum(x, 10) #coverts string x to a number
    num2 = baseBToNum(y, 10)
    num3 = num1 + num2
    final = numToBaseB(num3, 2)
    return final

assert add("11100", "11110") == '111010'
assert add("10101", "10101") == '101010'


def addB(S, T):
    """ addB takes in two strings and returns the sum of the two strings
        argument S: a string
        argument T: a string
    """
    # base cases!
    if len(S) == 0 and len(T) == 0:
        return ''
    if len(S) == 0 and len(T) != 0:
        return T
    if len(S) != 0 and len(T) == 0:
        return S
    # There will be four recursive cases--here is the first one:
    if S[-1] == '0' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '0'   # 0 + 0 == 0
    # three more recursive cases still to specify...
    if S[-1] == '1' and T[-1] == '0':
        return addB(S[:-1], T[:-1]) + '1'
    if S[-1] == '0' and T[-1] == '1':
        return addB(S[:-1], T[:-1]) + '1'
    if S[-1] == '1' and T[-1] == '1':
        return addB('1', addB(S[:-1], T[:-1])) + '0'
    
assert addB('11', '100') == '111'
assert addB("11100", "11110") == '111010'
assert addB('110','11') == '1001'
assert addB('110101010','11111111') == '1010101001'
assert addB('1','1') == '10'


def frontNum(S):
    '''frontNum takes in a string S and returns the number of times the front number
        char is repeated.
        argument S: a string
    '''
    if len(S) <= 1:
        return 1
    if S[0] == S[1]:
        return 1 + frontNum(S[1:])
    else:
        return 1

def compress(S):
    '''compress takes a string S and a returns a patern of binary numbers
       representing how many times a number is repeated.
       argument S: a string 
    '''
    if S == '':
        return ''
    else:
        x = frontNum(S) 
        y = numToBaseB(x, 2)
        z = 7 - len(y)
        return S[0] + '0' * z + y + compress(S[x:])

def uncompress(C):
    '''uncompress takes a compress string and returns what it wouldve been 
        without being compressed
        areugment C: a string
    '''
    if len(C) == 0:
        return ''
    else:
        x = baseBToNum(C[1:8], 2)
        return C[0] * x + uncompress(C[8:])




