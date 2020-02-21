#
# hw9pr1.py - Game of Life lab
#
# Name:
#

import random 

def createOneRow(width):
    """ returns one row of zeros of width "width"...  
         You might use this in your createBoard(width, height) function """
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """Returns a 2D array with "height" rows and "width" columns."""
    A = []
    for row in range(height):
        A += [width*createOneRow(width//height)]       # use the above function so that SOMETHING is one row!!
    return A

def printBoard(A):
    """This function prints the 2D list-of-lists A."""
    for row in A:               # row is the whole row
        for col in row:        # col is the individual element
            print(col, end='')  # print that element
        print()

def diagonalize(width, height):
    """Creates an empty board and then modifies it
       so that it has a diagonal strip of "on" cells.
       But do that only in the *interior* of the 2D array.
    """
    A = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

def innerCells(w, h):
    '''Creates a board with all centrealized positions set to 1
        and with all the edges set to 0
    '''
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = 1
    return A

def randomCells(w, h):
    A = createBoard(w, h)

    for row in range(1, h - 1):
        for col in range(1, w - 1):
            A[row][col] = random.choice([0,1])
    return A

def copy(A):
    """Returns a DEEP copy of the 2D array A."""
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            newA[row][col] = A[row][col]   # what single line should be here to copy each
                                           # element of A into the corresponding element of newA?
    return newA

def innerReverse(A):
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if A[row][col] == 0:
                newA[row][col] = 1
            else:
                newA[row][col] = 0          # what single line should be here to copy each
                                           # element of A into the corresponding element of newA?
    return newA

def countNeighbors(row, col, A):
    count = 0
    if A[row][col+1] == 1:
        count += 1
    if A[row][col-1] == 1:
        count += 1
    if A[row+1][col] == 1:
        count += 1
    if A[row+1][col+1] == 1:
        count += 1
    if A[row+1][col-1] == 1:
        count += 1
    if A[row-1][col+1] == 1:
        count += 1
    if A[row-1][col] == 1:
        count += 1
    if A[row-1][col-1] == 1:
        count += 1
    return count 

def next_life_generation(A):
    """Makes a copy of A and then advances one
       generation of Conway's Game of Life within
       the *inner cells* of that copy.
       The outer edge always stays at 0.
    """
    height = len(A)
    width = len(A[0])
    newA = createBoard(width, height)

    for row in range(1, height - 1):
        for col in range(1, width - 1):
            if countNeighbors(row, col, A) > 3 or countNeighbors(row, col, A) < 2:
                newA[row][col] = 0
            elif countNeighbors(row, col, A) == 3:
                newA[row][col] = 1
            else:
                newA[row][col] = A[row][col]
    return newA

    


















