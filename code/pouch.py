import numpy as np



class pouch(object):
    
    def __init__(self):        
        tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
        freqs = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]
        self.letters = []
        for i in range(len(tiles)):
            for j in range(freqs[i]):
                self.letters.append(tiles[i])

    def pick(self, player):  # picking new tiles for the player
        if len(self.letters) >= (7 - len(player.rack)):
            new_tiles = np.random.choice(self.letters, 7 - len(player.rack), replace=False)
            for i in new_tiles:
                player.rack.append(i)
                self.letters.remove(i)
        else:
            for i in self.letters:
                player.rack.append(i)
                self.letters.remove(i)

    def exchange(self, player, tiless):
        if len(self.letters) < 7:  # can exchange only if at least 7 tiles in the rack
            return False, 'Pouch has less than 7 letters. Cannot exchange.'  # indicates a failure of exchange
        new_tiles = np.random.choice(self.letters, len(tiless), replace=False)
        for i in new_tiles:
            self.letters.remove(i)
            player.rack.append(i)
        for i in tiless:
            player.rack.remove(i)
        return True, True  # indicates a successful exchange
        
    def loadpouch(self,board,racks):  # reconstructing a pouch from the saved racks of the players and the board
        boardtopouchdict_nonblanktiles= dict(zip(list(range(0, 26, 1)), string.ascii_uppercase))
        boardtopouchdict_blanktiles=dict(zip(list(range(26,52,1)), [' ']*26))
        boardtopouchdict={**boardtopouchdict_blanktiles,**boardtopouchdict_nonblanktiles}
        board_letters=list(map(lambda x: boardtopouchdict[x],board[board<52].tolist()))
        rack_letters=[item for sublist in racks for item in sublist]
        for i in board_letters+rack_letters:
            self.letters.remove(i)
