# board format: The board is an array of 15x15 shape, with the elements being numbers, 
# translated by the dictionary letternumberkey into strings whenever required.
import string

# letternumberkey dictionary to translate the integers on board to strings whenever necessary
l1 = dict(zip(string.ascii_uppercase, list(range(0, 26, 1))))
l2 = dict(zip(string.ascii_lowercase, list(range(26, 52, 1))))
letternumberkey = {**l1, **l2}
letternumberkey[' '] = 52
l3 = dict(zip(list(range(0, 26, 1)), string.ascii_uppercase))
l4 = dict(zip(list(range(26, 52, 1)), string.ascii_lowercase))
numberletterkey = {**l3, **l4}
numberletterkey[52] = ' '

# arguments: letters is a list of numbers representing string characters which you want to place on the board, 
# positions is a list of lists with each sublist containing two numbers indicating the position of the 
# corresponding letters on the board array, player is the player making the move.

def move(letters, positions, player, mainboard):
    board = mainboard.copy()
    for i in range(len(letters)):
        board[positions[i][0], positions[i][1]] = letternumberkey[letters[i]]
        if letters[i] == letters[i].upper():
            player.rack.remove(letters[i])
        else:
            player.rack.remove(' ')
    return board
