# A Connect Four Board class
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
# AI Player for use in Connect Four 
#
# Developed as part of an academic project in CS112 at Boston University
# 

import random  
from ps9pr3 import *

class AIPlayer(Player):
    
    def __init__(self, checker, tiebreak, lookahead):
        '''constructs a new AIPlayer object
        '''
        #validate the inputs
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        #initialize the inherited attributes from superclass
        super().__init__(checker)
        
        #initialize the attributes that are not inherited from Player
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        '''returns a string representing an AIPlayer object.
        '''
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', '  + str(self.lookahead) + ')'
    
    
    def max_score_column(self, scores):
        '''takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score.
        scores: input a list of int's "scores"
        '''
        best_score = 0
        col_choices = []
        for i in scores:
            best_score = max(scores)
            
        for i in range(len(scores)):
            if scores[i] == best_score:
                col_choices += [i]
                
        if self.tiebreak == 'LEFT':
            return col_choices[0]
        elif self.tiebreak == 'RIGHT':
            return col_choices[-1]
        else:
            if self.tiebreak == 'RANDOM':
                return random.choice(col_choices)
            
        
    def scores_for(self, b):
        '''takes a Board object b and determines the called AIPlayer‘s scores 
        for the columns in b. The method returns a list containing one score 
        for each column. 
        b: input a Board object
        '''
        scores = [-2]* b.width
        
        #loop through each column and determine the score for each
        for i in range(b.width):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker) == True:
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                #look ahead for the scores of the opponent
                b.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(b)                    
                if max(opp_scores) == 100:
                    scores[i] = 0
                elif max(opp_scores) == 0:
                    scores[i] = 100
                else: 
                    scores[i] = 50
                #Remove the checker that was placed in this column
                b.remove_checker(i)
            
        return scores 
    
    
    def next_move(self, b):
        '''return the called AIPlayer‘s judgment of its best possible move.
        '''
        return self.max_score_column(self.scores_for(b))
        
        
                
                
            
            
        
        
