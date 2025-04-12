# A Connect Four Board class
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
#
# Developed as part of an academic project in CS112 at Boston University
# 

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b


def process_move(p, b):
    '''takes two parameters: a Player object p for the player whose move is 
    being processed, and a Board object b for the board on which the game is 
    being played. And will process the moves. 
    p: input a Player object
    b: input a Board object 
    '''
    print('Player' + p.checker + "'s turn")
    
    #Obtain player p‘s next move and process it
    next_col_move = p.next_move(b)
    b.add_checker(p.checker, next_col_move)
    print('\n')
    print(b)
    
    #Check to see if the move resulted in a win or a tie
    if b.is_win_for(p.checker) == True:
        print('Player ' + p.checker + ' wins in ' + str(p.num_moves) + ' moves.' + '\n' + 'Congratulations!')
        return True
    #How to check for tie??????****
    elif b.is_full() == True:
            print("It's a tie!")
            return True
    else:
        return False


class RandomPlayer(Player):
    
    def next_move(self, b):
        '''chooses at random from the columns in the board b that are not yet 
        full, and return the index of that randomly selected column. 
        b: input board b
        '''
        available_col = []
        count = 0
        for x in range(b.width):
            if b.can_add_to(x) == True:
                available_col += [x]
                count += 1
        random_index = random.choice(available_col)
        #increment the number of moves that the RandomPlayer object has made
        self.num_moves += 1
        return random_index
        

        
        

    
    

    
    
    

