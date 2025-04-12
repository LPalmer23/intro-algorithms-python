# A Connect Four Board class
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
#
# Developed as part of an academic project in CS112 at Boston University
#

from ps9pr1 import Board

# write your class below.
class Player:
    
    def __init__(self, checker):
        '''constructs a new Player object by initializing the following two 
        attributes: a one-character string for the player (checker) and 
        an integer that stores how many moves the player has made so 
        far (num_moves) 
        checker: input a one-character string
        '''
        #an assert statement that validates the input for checker
        assert(checker == 'X' or checker == 'O')
        
        #initialize attributes
        self.checker = checker
        self.num_moves = 0
        
        
    def __repr__(self):
        '''returns a string representing a Player object. The string returned 
        should indicate which checker the Player object is using.
        '''
        return 'Player ' + str(self.checker)
    

    def opponent_checker(self):
        '''returns a one-character string representing the checker of the Player 
        object’s opponent. The method may assume that the calling Player object 
        has a checker attribute that is either 'X' or 'O'.
        '''
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
        
    def next_move(self, b):
        '''accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move. 
        b: input a board object 
        '''
        move = int(input('Enter a column: '))
        while b.can_add_to(move) == False:
            print('Try again!')
            move = int(input('Enter a column: '))
            
        #increment the number of moves that the Player object has made.
        self.num_moves += 1
        return int(move)
        
 
        
        
        
        
        
        
        
        
        
        
        
        
    
