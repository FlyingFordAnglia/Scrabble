from player import player
from pouch import pouch
from savegame import savegame, loadgame
from gamerulechecker import mainrules
import numpy as np
from scorer import scorer, endscore
from modify import move


class GameEngine(object):

    def __init__(self, playernames=None, gamestatus='new', validity_mode=True, filename='wordlist/sowpods.txt', savefilename='savegame.sv'):
        if gamestatus == 'new':
            self.filename = filename  # file to check for the validity of the word if validity mode is on
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
            savedgame = loadgame(savefilename)
            self.board = savedgame[0]
            self.numberofplayers = len(savedgame[1])
            self.players = list(map(player, savedgame[3], savedgame[2], savedgame[1]))
            self.turn = savedgame[4]
            self.pouch = pouch()
            self.pouch.loadpouch(self.board, savedgame[1])

    def exchange(self, tiles_to_exchange):
        for i in tiles_to_exchange:
            if tiles_to_exchange.count(i) > self.players[self.turn].rack.count(i):
                return False, 'You do not have this tile to exchange it.'
        resp = self.pouch.exchange(self.players[self.turn], tiles_to_exchange)
        if resp[0]:
            self.turn += 1
            self.turn %= self.numberofplayers  # updating turn
            return True, True
        else:
            return False, resp[1]

    def scrabbleit(self, playerinput):
        validity = mainrules(playerinput, self.board, self.players[self.turn].rack, validity=self.validitymode, filename=self.filename)   # verifying validity of move
        if validity[0]:
            gameended = False
            self.players[self.turn].score += scorer(validity[1], validity[2], self.board)  # updating score of player
            moveboard = move(validity[1][0], validity[1][1], self.players[self.turn], self.board)  # updating board
            self.board = moveboard
            if len(self.pouch.letters) > 0:
                self.pouch.pick(self.players[self.turn])  # picking new tiles
            else:
                if len(self.players[self.turn].rack) == 0:  # if the game ends by the rack of a person going empty
                    endscore(self.players, self.turn)
                    gameended = True
            self.turn += 1
            self.turn %= self.numberofplayers  # updating turn
            return True, gameended
        else:
            return False, validity[2]
    
    def save(self, filename='savegame.sv'):
        savegame(self.board, [i.rack for i in self.players], self.players, self.turn, filename)
