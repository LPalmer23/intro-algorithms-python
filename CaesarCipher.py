# Caesar cipher / decipher
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
# Encrypts and decrypts text using the Caesar cipher with recursion and letter frequency scoring.
# Includes functions for rotating letters, encoding messages, and automatically deciphering them.
#
# Developed as part of an academic project in CS112 at Boston University

def rotate(c, n):
    """Takes as inputs a single character c and a non-negative integer n 
    between 0 and 25, and that returns a single character that is based on c. 
    If c is a letter of the alphabet, the function should “rotate” it by n 
    characters forward in the alphabet, wrapping around as needed.
    c: input string (single character)
    n: input integer (non-negative between 0-25)
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)


    if 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)
    return chr(new_ord)



def encipher(s, n):
    '''Takes as inputs an arbitrary string s and a non-negative integer n 
    between 0 and 25, and that uses recursion to create and return a new 
    string in which the letters in s have been “rotated” by n characters 
    forward in the alphabet, wrapping around as needed.
    s: input string
    n: input integer (non-negative between 0-25)
    '''
    if len(s) == 0:
        return ''
    else:
        enci_rest = encipher(s[1:], n)
        return rotate(s[0], n) + enci_rest



# A helper function

def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0


def string_score(s):
    '''Takes an arbitrary string s and that uses either recursion OR a list 
    comprehension to compute and return the sum of the letter-score values 
    of the characters in s.
    s: input string
    '''
    return sum(letter_score(x) for x in s)

def decipher(s):
    '''Takes as input an arbitrary string s that has already been enciphered 
    by having its characters “rotated” by some amount (possibly 0). The 
    function should return, to the best of its ability, the original English 
    string, which will be some rotation (possibly 0) of the input string s.
    s: input string
    '''
    options = [encipher(s, n) for n in range(26)]
    scored_words = [[string_score(x), x] for x in options]
    return max(scored_words)[1]


    
print(decipher('sourp'))
    
    
    
    
    
    
    
    
    
    
    
    
    

    

