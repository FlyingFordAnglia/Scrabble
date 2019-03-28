from player import player
from pouch import pouch
from savegame import savegame, loadgame
from gamerulechecker import mainrules
import numpy as np
from scorer import scorer
from modify import move


class GameEngine(object):

    def __init__(self, playernames=None, gamestatus='new', validity_mode=True, filename='wordlist/sowpods.txt'):
        if gamestatus == 'new':
            self.filename = filename
            self.validitymode = validity_mode
            self.board = np.zeros([15, 15], dtype=int) + 52  # empty board
            self.numberofplayers = len(playernames)
            self.players = list(map(player, playernames))
            self.turn = 0
            self.pouch = pouch()
            for x in self.players:
                self.pouch.pick(x)
        else:
            self.filename = filename
            self.validitymode = validity_mode
            savedgame = loadgame(filename)
            self.board = savedgame[0]
            self.numberofplayers = len(savedgame[1])
            self.players = list(map(player, (savedgame[3], savedgame[2], savedgame[1])))

            self.turn = savedgame[4]
            self.pouch = pouch()
            self.pouch.loadpouch(self.board, savedgame[1])

    def scrabbleit(self, playerinput):
        validity = mainrules(playerinput, self.board, validity=self.validitymode, filename=self.filename)   # verifying validity of move
        if validity[0]:
            self.players[self.turn].score += scorer(validity[1], validity[2], self.board)  # updating score of player
            self.board = move(validity[1][0], validity[1][1], self.players[self.turn], self.board)  # updating board
            self.pouch.pick(self.players[self.turn])  # picking new tiles
            self.turn += 1
            self.turn %= self.numberofplayers  # updating turn
            return True
        else:
            return False
    
    def save(self, filename='savegame.sv'):
        savegame(self.board, [i.rack for i in self.players], self.players, self.turn, filename)
