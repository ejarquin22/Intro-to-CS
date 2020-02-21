# CS5, hw2pr3
# Filename: hw2pr3.py
# Name:
# Problem description: Function Frenzy!

#
# leng example from class
#
def leng(s):
    """leng returns the length of s
       Argument: s, which can be a string or list
    """
    if s == '' or s == []:   # if empty string or empty list
        return 0
    else:
        return 1 + leng(s[1:])


def flipside(s):
  """flipside swaps s's sides
     Argument s: a string
  """
  x = len(s)//2
  return s[x:] + s[:x]

#
# Tests
#
assert flipside('carpets')  == 'petscar'
assert flipside('homework') == 'workhome'
assert flipside('flipside') == 'sideflip'
assert flipside('az')       == 'za'
assert flipside('a')        == 'a'
assert flipside('')         == ''

def mult(n, m):
    '''mult multiplies m times n
        Argument n: a number (int or float)
        Argument m: a number (int or float)
    '''
    if m == 0:
        return 0
    elif m > 0:
        return n + mult(n, m-1)
    elif m < 0:
        return -n + mult(n, m+1)
#
# Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0

def dot(L, K):
    '''dot returns the dot product of vectors L and K
        Argument L: a non-empty list
        Argument K: a non-empty list
    '''
    if len(L) != len(K):
        return 0.0
    if L == [] or K == []:
        return 0.0
    elif L[0] != [] and K[0] != []:
        return L[0] * K[0] + dot(L[1:], K[1:])
    else:
        return L[1:] * K[1:]
#
# Tests
#
assert dot([5, 3], [6, 4])                       == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6])                          == 0.0
assert dot([], [6])                              == 0.0
assert dot([], [])                               == 0.0

def ind(e, L):
    '''ind returns the index in a list L containing
        a value equal to element C
        Argument e: an element (string or int)
        Argument L: a sequence (int, string, list)
    '''
    if e not in L:
        return len(L)
    if e in L:
        if L[0] == e:
            return 0
        else:
            return 1 + ind(e, L[1:])

#
# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5

def letterScore(let):
    '''letterScore returns an assigned value for any lower case letter
        Argument let: a string
    '''
    if let in 'aeilnorstu':
        return 1
    if let in 'dg':
        return 2
    if let in 'bcmp':
        return 3
    if let in 'fhvwy':
        return 4
    if let in 'k':
        return 5
    if let in 'jx':
        return 8
    if let in 'qz':
        return 10
    if let not in 'abcdefghijklmnopqrstuvwxyz':
        return 0

def scrabbleScore(S):
    '''scrabbleScore returns the value of all letters in a string
        added up
        Argument S: a string
    '''
    if S == '':
        return 0
    if S[0] in 'abcdefghijklmnopqrstuvwxyz':
        return letterScore(S[0]) + scrabbleScore(S[1:])
    else:
        return 0

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0

def one_dna_to_rna(c):
    """Converts a single-character c from DNA
        nucleotide to complementary RNA nucleotide """
    if c == 'A':
        return 'U'
    if c == 'C':
        return 'G'
    if c == 'G':
        return 'C'
    if c == 'T':
        return 'A'
    else:
        return ''

def transcribe(S):
    '''transctibe swaps ACGT to UGCA accordingly and removes any spaces
        Argument S: a string
    '''
    if S == '':
        return ''
    if S[0] in 'ACGT':
        return one_dna_to_rna(S[0]) + transcribe(S[1:])
    else:
        return transcribe(S[1:])

#
# Tests
#
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU' # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that the other characters disappear
assert transcribe('')         == ''
