def inarow_Neast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading east and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsouth(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading south and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nnortheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading northeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start - (N-1) < 0 or r_start > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start-i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True

def inarow_Nsoutheast(ch, r_start, c_start, A, N):
    """Starting from (row, col) of (r_start, c_start)
       within the 2d list-of-lists A (array),
       returns True if there are N ch's in a row
       heading southeast and returns False otherwise.
    """
    H = len(A)
    W = len(A[0])
    if r_start < 0 or r_start + (N-1) > H - 1:
        return False # out of bounds row
    if c_start < 0 or c_start + (N-1) > W - 1:
        return False # o.o.b. col
    # loop over each location _offset_ i
    for i in range(N):
        if A[r_start+i][c_start+i] != ch: # a mismatch!
            return False
    return True  # all offsets succeeded, so we return True



class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

        # We do not need to return anything from a constructor!

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''                          # the string to return
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # bottom of the board

        # and the numbers underneath here

        return s       # the board is complete, return it

    def addMove(self, col, ox):
        '''sets an X or O any specified column on the board
        '''
        for row in range(0, self.height):
            if self.data[row][col] != ' ':
                self.data[row-1][col] = ox
                return
        self.data[self.height-1][col] = ox
    
    def setBoard(self, moveString):
        """Accepts a string of columns and places
           alternating checkers in those columns,
           starting with 'X'.

           For example, call b.setBoard('012345')
           to see 'X's and 'O's alternate on the
           bottom row, or b.setBoard('000000') to
           see them alternate in the left column.

           moveString must be a string of one-digit integers.
        """
        nextChecker = 'X'   # start by playing 'X'
        for colChar in moveString:
            col = int(colChar)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X':
                nextChecker = 'O'
            else:
                nextChecker = 'X'

    def allowsMove(self, col):
        '''returns true if the move being made is a legal one
            and returns false otherwise
        '''
        if col < 0 or col >= self.width:
            return False
        if self.data[0][col] != ' ':
            return False
        else:
            return True

    def isFull(self):
        '''returns True if the board is Full and Flase if it is not
        '''
        for x in self.data:
            for y in x:
                if y == ' ':
                    return False
        return True
    
    def delMove(self, c):
        '''deletes the top piece in a col
        '''
        for x in range(self.height):
            if self.data[x][c] != ' ':
                self.data[x][c] = ' '
                return
    
    def winsFor(self, ox):
        '''checks horizontally, vertically, and diagonally for a winner
        '''
        x = self.data
        for row in range(self.height):
            for col in range(self.width-3):
                if x[row][col] == ox and x[row][col+1] == ox and x[row][col+2] == ox and x[row][col+3] == ox:
                    return True
        
        for col in range(self.width):
            for row in range(self.height-3):
                if x[row][col] == ox and x[row+1][col] == ox and x[row+2][col] == ox and x[row+3][col] == ox:
                    return True

        for row in range(self.height-3):
            for col in range(self.width-3):
                if x[row][col] == ox and x[row+1][col+1] == ox and x[row+2][col+2] == ox and x[row+3][col+3] == ox:
                    return True       

        for row in range(self.height-3):
            for col in range(3, self.width):
                if x[row][col] == ox and x[row+1][col-1] == ox and x[row+2][col-2] == ox and x[row+3][col-3] == ox:
                    return True   
        return False

    def hostGame(self):
        '''Creates and interactive game that will always let X go first, and then O go after.
            After each move, the board will be printed. It will end when the board is full or
            if there is a winner.
        '''
        print("Welcome to Connect Four!\n")
        print(self)
        while True:
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("X, Choose a column: "))
            self.addMove(users_col, 'X')
            print(self)
            if self.winsFor('X') == True:
                print("X wins!")
                print(self)
                break
            users_col = -1
            while not self.allowsMove(users_col):
                users_col = int(input("O, Choose a column: "))
            self.addMove(users_col, 'O')
            print(self)
            if self.winsFor('O') == True:
                print("O wins!")
                print(self)
                break       
            if self.isFull() == True:
                print("It's A Tie..")
                break
