import numpy as np

tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
freqs = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]


class pouch(object):

    def __init__(self):
        self.letters = []
        for i in range(len(tiles)):
            for j in range(freqs[i]):
                self.letters.append(tiles[i])

    def pick(self, player):
        if len(self.letters) >= (7 - len(player.rack)):
            new_tiles = np.random.choice(self.letters, 7 - len(player.rack), replace=False)
            for i in new_tiles:
                player.rack.append(i)
                self.letters.remove(i)
            print('Tiles left in pouch = ', len(self.letters))
        else:
            for i in self.letters:
                player.rack.append(i)
                self.letters.remove(i)
            print('The pouch is empty.')

    def exhange(self, player, tiless):
        if len(self.letters) < 7:  # can exchange only if at least 7 tiles in the rack
            return False  # indicates a failure of exchange
        new_tiles = np.random.choice(self.letters, len(tiless), replace=False)
        for i in new_tiles:
            self.letters.remove(i)
            player.rack.append(i)
        for i in tiless:
            player.rack.remove(i)
            return True  # indicates a successful exchange
