# player input is: Word made, starting tile position of the word made, horizontal or vertical
# example: playerinput = ['STRING', (0, 1), 'v']
import numpy as np
import string

def boundarytester(playerinput):  # to check whether the player is placing the tiles in the confines of the board
    if playerinput[1][0] > 14 or playerinput[1][0] < 0 or playerinput[1][1] > 14 or playerinput[1][1] < 0:
        return False
    if playerinput[2] == 'h':
        if (playerinput[1][1] + len(list(playerinput[0]))) > 14:
            return False
    if playerinput[2] == 'v':
        if (playerinput[1][0] + len(list(playerinput[0]))) > 14:
            return False
    return True


def moveconverter(playerinput, board):  # converting player input to internal lingo for a move
    word = list(playerinput[0])
    if playerinput[2] == 'v':
        # p is the list of positions of the tiles in word made
        p = [(x, playerinput[1][1]) for x in range(playerinput[1][0], playerinput[1][0] + len(word))]
        # bmask is a boolean mask to find out which positions are not occupied on the board
        bmask = board[p[0][0]:p[-1][0]+1, p[0][1]] == 52
        letters = np.array(word)[bmask].tolist()
        positions = np.array(p)[bmask].tolist()

    elif playerinput[2] == 'h':
        p = [(playerinput[1][0], x) for x in range(playerinput[1][1], playerinput[1][1] + len(word))]
        bmask = board[p[0][0], p[0][1]:p[-1][1]+1] == 52
        letters = np.array(word)[bmask].tolist()
        positions = np.array(p)[bmask].tolist()

    return letters, positions

# This function takes the positions of the letters placed on the board, and returns a list of the words made
# by the placement of the letters. The format of the returned list is that it is a list of tuples, each a word
# represented by the positions of the corresponding letters.
def wordsmade(letters, positions, mainboard):
    l1 = dict(zip(string.ascii_uppercase, list(range(0, 26, 1))))
    l2 = dict(zip(string.ascii_lowercase, list(range(26, 52, 1))))
    letternumberkey = {**l1, **l2}
    letternumberkey[' '] = 52
    board = mainboard.copy()
    for i in range(len(letters)):
        board[positions[i][0], positions[i][1]] = letternumberkey[letters[i]]
    wordsp = []
    for i in positions:
        # Horizontally
        ph = np.array(list(zip([i[0]] * 15, list(range(0, 15)))))[board[i[0], :] < 52].tolist()
        # a list of all occupied places on the board
        r = list(map(tuple, ph))
        # Trimming the list so that any places after an unoccupied place from the placed letters are removed.
        if len(r) > 1:
            for j in range(r.index(tuple(i)), 0, -1):
                if (r[j][1] - r[j - 1][1]) > 1:
                    r = r[j:]
                    break
            for j in range(r.index(tuple(i)), len(r), 1):
                try:
                    if (r[j + 1][1] - r[j][1]) > 1:
                        r = r[:j + 1]
                        break
                except IndexError:
                    pass
            if len(r) > 1:
                wordsp.append(r)

        # Vertically
        pv = np.array(list(zip(list(range(0, 15)), [i[1]] * 15)))[board[:, i[1]] < 52].tolist()
        s = list(map(tuple, pv))
        if len(s) > 1:
            for j in range(r.index(tuple(i)), 0, -1):
                if (r[j][0] - r[j - 1][0]) > 1:
                    r = r[j:]
                    break
            for j in range(r.index(tuple(i)), len(r), 1):
                try:
                    if (r[j + 1][0] - r[j][0]) > 1:
                        r = r[:j + 1]
                        break
                except IndexError:
                    pass
            if len(s) > 1:
                wordsp.append(s)
    wordspq = []
    for i in wordsp:
        wordspq.append(tuple(i))

    return list(set(wordspq))  # Set is used here to remove redundant words.


def validword(words, filename='wordlist/sowpods.txt'):
    with open(filename, 'r') as f:
        rd = f.read()
        rd = rd.split('\n')
        rd = rd[0:len(rd) - 1]
    rd = set(rd)
    for j in words:
        if j not in rd:
            return False
    return True


def overlaptester(playerinput,board):
    l_1 = dict(zip(list(range(0, 26, 1)), string.ascii_uppercase))
    l_2 = dict(zip(list(range(26, 52, 1)), string.ascii_lowercase))
    numberletterkey = {**l_1, **l_2}
    numberletterkey[52] = ' '
    word = playerinput[0]
    if playerinput[2] == 'v':
        p = [(x, playerinput[1][1]) for x in range(playerinput[1][0], playerinput[1][0] + len(word))]
        # bmask is a boolean mask to find out which positions are occupied on the board
        bmask = board[p[0][0]:p[-1][0]+1, p[0][1]] != 52
        overlapletters = ''.join(np.array(list(word))[bmask].tolist()).lower()
        existingletters = ''.join(list(map(lambda x: numberletterkey[x], board[p[0][0]:p[-1][0]+1, p[0][1]][bmask]))).lower()
        if overlapletters != existingletters:
            return False
    elif playerinput[2] == 'h':
        p = [(playerinput[1][0], x) for x in range(playerinput[1][1], playerinput[1][1] + len(word))]
        bmask = board[p[0][0], p[0][1]:p[-1][1]+1] != 52
        overlapletters = ''.join(np.array(list(word))[bmask].tolist()).lower()
        existingletters = ''.join(list(map(lambda x: numberletterkey[x], board[p[0][0], p[0][1]:p[-1][1]+1][bmask]))).lower()
        if overlapletters != existingletters:
            return False
    return True


def mainrules(playerinput, board, validity=True, filename='wordlist/sowpods.txt'):
    l_1 = dict(zip(list(range(0, 26, 1)), string.ascii_uppercase))
    l_2 = dict(zip(list(range(26, 52, 1)), string.ascii_lowercase))
    numberletterkey = {**l_1, **l_2}
    numberletterkey[52] = ' '
    l1 = dict(zip(string.ascii_uppercase, list(range(0, 26, 1))))
    l2 = dict(zip(string.ascii_lowercase, list(range(26, 52, 1))))
    letternumberkey = {**l1, **l2}
    letternumberkey[' '] = 52
    if not boundarytester(playerinput):
        return False, False, False
    if not overlaptester(playerinput,board):
        return False, False, False
    move = moveconverter(playerinput, board)
    words = wordsmade(move[0], move[1], board)
    internal_board = board.copy()
    for i in range(len(move[0])):
        internal_board[move[1][i][0], move[1][i][1]] = letternumberkey[move[0][i]]
    actual_words = []
    for i in words:
        w = []
        for j in i:
            w.append(numberletterkey[internal_board[j[0], j[1]]])
        actual_words.append(''.join(w).lower())
    if validity:
        if not validword(actual_words, filename):
            return False, False, False
    return True, move, words
