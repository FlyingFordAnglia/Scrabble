import numpy as np

tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ ')
freqs = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]


class pouch(object):
    number_of_tiles = 100
    max_letters_per_turn = 7

    def __init__(self):
        self.letters = []
        for i in range(len(tiles)):  # easier to read than a nested list comprehension
            for j in range(freqs[i]):
                self.letters.append(tiles[i])

    def pick(self, rack):
        if len(self.letters) >= (7 - len(rack)):
            new_tiles = np.random.choice(self.letters, 7 - len(rack), replace=False)
            for i in new_tiles:
                rack.append(i)
                self.letters.remove(i)
            print('Tiles left in pouch = ', len(self.letters))
        else:
            for i in self.letters:
                rack.append(i)
                self.letters.remove(i)
            print('The pouch is empty.')
