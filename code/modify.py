# board format: The board is an array of 15*15 shape, with the elements being numbers, 
# translated by the dictionary letternumberkey into strings whenever required.
import string

# letternumberkey dictionary to translate the integers on board to strings whenever necessary
l1 = dict(zip(string.ascii_uppercase, list(range(0, 26, 1))))
l2 = dict(zip(string.ascii_lowercase, list(range(26, 52, 1))))
letternumberkey = {**l1, **l2}
letternumberkey[' '] = 52

# arguments: letters is a list of string characters which you want to place on the board, 
# positions is a list of lists with each sublist containing two numbers indicating the position of the 
# corresponding letters on the board array, player is the player making the move.

def move(letters, positions, player, mainboard):
    board = mainboard.copy()
    for i in range(len(letters)):
        board[positions[i][0], positions[i][1]] = letternumberkey[letters[i]]
        player.rack.remove(letters[i])
    return board