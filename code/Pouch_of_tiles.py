import numpy as np
class pouch(object):
    number_of_tiles = 100
    max_letters_per_turn=7

    def __init__(self):
        self.letters=[item for sublist in [['A']*9, ['B']*2, ['C']*2, [' ']*2] for item in sublist]
        #flatten the sublist of each letter
    def pick(self,rack):
        if len(self.letters)>= (7-len(rack)):
            new_tiles=np.random.choice(self.letters,7-len(rack),replace=False).tolist()
            #replace is if you want the samples to be returned to the list for next sampling
            #tolist because random choice returns an array
            for i in new_tiles:
                rack.append(i)
                self.letters.remove(i)
            print('Tiles left in pouch = ', len(self.letters))
        else:
            for i in self.letters:
                rack.append(i)
                self.letters.remove(i)
            print('The pouch is empty')


#racks can just be simple lists. No need to create a class for them. The class player can have rack as part of it along with the score.
