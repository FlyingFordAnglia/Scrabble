#board format: The board is an array of 15*15 shape, with the elements being numbers, translated by the dictionary letternumberkey into strings whenever required.

board=numpy.zeros([15,15],dtype=int)+52

#rack format:
#rack=[]
#len(rack)=7

#letternumberkey dictionary to translate the integers on board to strings whenever necessary
l1=dict(zip(string.ascii_uppercase,list(range(0,26,1))))
l2=dict(zip(string.ascii_lowercase,list(range(26,52,1))))
letternumberkey={**l1,**l2}
letternumberkey[' ']=52


#move funtcion

#arguments: letters is a list of string characters which you want to place on the board, positions is a list of lists with each sublist containing two numbers indicating the position of the corresponding letters on the board array, rack is the rack from which the letters are taken.

def move(letters, positions, rack):
    assert len(letters) == len(positions), 'Please specify where each letter goes'
    for i in range(len(letters)):
        try:
            rack.index(letters[i])
        except ValueError:
            print('The letters you chose are not in your rack')

        board[positions[i][0],positions[i][1]] = letternumberkey[letters[i]]
        rack.remove(letters[i])
