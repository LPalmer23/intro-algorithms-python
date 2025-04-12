# A Connect Four Board class
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
#
# Developed as part of an academic project in CS112 at Boston University
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   


    def __init__(self, height, width):
        '''constructs a new Board object by initializing the following three 
        attributes: number of rows (height), number of columns (width), and a
        two-dimentional reference (slots)
        height: input num of rows
        width: input num of columns
        '''
        #initialize the following three attributes:
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row    
            

        
        # a line of hyphen characters (-)
        s += '-' * (self.width*2 + 1) + '\n'
        
        # a line of numeric column labels for all of the columns
        for i in range(self.width):
            s += ' ' + str(i)[-1]
     
        return s



    def add_checker(self, checker, col):
        """accepts a one-character string "checker" of either "X" or "O" and a 
           "col" integer that specifies which index to place the move. And 
           then places the checker there.
           insert checker: input a one-character string (either 'X' or 'O')
           insert col: an integer for chosen column
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

    # put the rest of the method here
        row = 0
        for i in range(self.height - 1):
            if self.slots[row+1][col] == ' ':
                row += 1
        self.slots[row][col] = checker

        
        
    ### add your reset method here ###
    def reset(self):
        '''reset the Board object on which it is called by setting all slots 
        to contain a space character.
        '''
        self.slots = [[' '] * self.width for row in range(self.height)]
    
    
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            columns: input a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column col on 
        the calling Board object. Otherwise, it should return False.
        col: ELABORATE
        '''
        if col in range(self.width) and self.slots[0][col] == ' ':
            return True
        else:
            return False
            
        
        
    def is_full(self):
        '''returns True if the called Board object is completely full of 
        checkers, and returns False otherwise.
        '''
        count = 0
        for i in range(self.width):
            if self.can_add_to(i) == True:
                count += 1
        if count > 0:
            return False
        else:
            return True 
        
        
        
    def remove_checker(self, col):
        '''removes the top checker from column col of the called Board object.
        If the column is empty, then the method should do nothing.
        col: input int for chosen column
        '''
        i = 0
        while i < self.height: 
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                break
            i += 1

    
    
    def is_win_for(self, checker):
        '''accepts a parameter checker that is either 'X' or 'O', and returns 
        True if there are four consecutive slots containing checker on the 
        board. Otherwise, it should return False.
        checker: insert string of either 'X' or 'O'
        '''
        
        #an assert statement that validates the input for checker
        assert(checker == 'X' or checker == 'O')
        
        #Checks if there are four consecutive "checker"s horizontally
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        
        #Checks if there are four consecutive "checker"s vertically
        for row in range(self.height-3):
            for col in range(self.width):
            # Check if the next four rows in this column
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                       return True
                   
        #Checks if there are four consecutive "checker"s diagonally downward            
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Checks for diagonal downwards win
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                       return True
        
        
        #Checks if there are four consecutive "checker"s diagonally upward            
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Checks for diagonal upwards win
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                       return True

    # if we make it here, there were no wins
        return False



        
        
            
            
        
            
            
           
            
            
         
        
                

                
                
                
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
