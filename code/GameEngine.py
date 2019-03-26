class GameEngine(object):

    def __init__(self, playernames=('1', '2', '3', '4'), gamestatus='new', filename='savegame.sv'):
        if gamestatus == 'new':
            self.board = numpy.zeros([15, 15], dtype=int) + 52
            self.numberofplayers = len(playernames)
            players = list(map(player, playernames))
            self.turn = 0
            self.pouch = pouch()
            map(lambda x: self.pouch.pick(x), players)

        else:
            savedgame = loadgame(filename)
            self.board = savedgame[0]
            self.numberofplayers = len(savedgame[1])
            players = list(map(player, (savedgame[3], savedgame[2], savedgame[1])))
            self.turn = savedgame[4]
            self.pouch = pouch()
            self.pouch.loadpouch(self.board, savedgame[1])

    def scrabbleit(self, playerinput):
        validity = gamerulechecker(playerinput)   #Verifying validity of move
        if validity[0]:
            players[playerinput[3]].score += scorer(validity[1], board) #Updating score of player
            self.board = move(validity[1][0], validity[1][1], players[playerinput[3]], self.board)    #Updating board
            self.pouch.pick(players[playerinput[3]])    #Picking new tiles
            self.turn += 1
            self.turn %= 3    #Updating turn
            return True
        else:
            return False
