# Save game to and load game from file
import numpy as np


def savegame(board, racks, players, turn, filename='savegame.sv'):
    # create header for the active racks, player scores, players names, and the active turn
    racks = list(map(lambda x: ''.join(x), racks))  # for each rack, make it into a single string
    racks = ';'.join(racks) + ':'  # combine all racks into a string
    scores = [str(i.score) for i in players]
    scores = ';'.join(scores) + ':'  # single string for player scores
    names = [i.name for i in players]
    names = ';'.join(names) + ':'  # single string for player names
    turn = str(turn)
    np.savetxt(filename, board, header=racks + scores + names + turn, fmt='%d', delimiter=',')


def loadgame(filename='savegame.sv'):
    # load from header
    with open(filename, 'r') as f:
        header = f.readline()
        header = header[2:len(header)]  # remove the "comment" prefix added to headers by np.savetxt()
        header = header.split(':')
        racks = header[0].split(';')
        racks = list(map(list, racks))  # each rack was stored as a single string; this makes it into a list
        scores = header[1].split(';')
        scores = list(map(int, scores))
        names = header[2].split(';')
        turn = int(header[3])
        board = []
        for i in f:  # load the board
            board.append(list(map(int, i.split(','))))
        board = np.array(board, dtype=int)
        return board, racks, scores, names, turn
