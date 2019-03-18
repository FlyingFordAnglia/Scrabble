
# player input is: Word made, starting tile position of the word made, horizontal or vertical, which player
#example: playerinput = ['STRING', (0, 1), 'v', player]


def boundarytester(playerinput):  #this is to check whether the player is placing the tiles in the confines of the board
    if playerinput[1][0] > 14 or playerinput[1][0] < 0 or playerinput[1][1] > 14 or playerinput[1][1] < 0:
        return False
    if playerinput[2] == 'h':
        if (playerinput[1][1] + len(list(playerinput[0]))) > 14:
            return False
    if playerinput[2] == 'v':
        if (playerinput[1][0] + len(list(playerinput[0]))) > 14:
            return False


def moveconverter(playerinput, board):  #converting player input to internal lingo for a move
    word = list(playerinput[0])
    if playerinput[2] == 'v':
    
    #p is the list of positions of the tiles in word made
    
        p = list(zip(list(range(playerinput[1][0], playerinput[1][0] + len(word))), [playerinput[1][1]] * len(word)))
        
    #bmask is a boolean mask to find out which positions are not occupied on the board
    
        bmask = board[playerinput[1][0]:playerinput[1][0] + len(word), playerinput[1][1]] == 52
        
        letters = np.array(word)[bmask].tolist()
        positions = np.array(p)[bmask].tolist()
        
    if playerinput[2] == 'h':
    
        p = list(zip([playerinput[1][0]] * len(word), list(range(playerinput[1][1], playerinput[1][1] + len(word)))))
        bmask = board[playerinput[1][0], playerinput[1][1]:playerinput[1][1] + len(word)] == 52
        letters = np.array(word)[bmask].tolist()
        positions = np.array(p)[bmask].tolist()
        
    return letters, positions


letters = moveconverter(playerinput, board)[0]
positions = moveconverter(playerinput, board)[1]


#This function takes the positions of the letters placed on the board, and returns a list of the words made by the placement of the letters. 
#The format of the returned list is that it is a list of tuples, each a word represented by the positions of the corresponding letters.


#This function should be used after the letters are placed on the mainboard, and not before.
def wordsmade(positions,board):
    wordsp = []
    for i in positions:
        #Horizontally
        ph = np.array(list(zip([i[0]] * 15, list(range(0, 15, 1)))))[board[i[0], :] < 52].tolist()  #a list of all occupied places on the board
        r = []
        for j in ph:
            r.append(tuple(j))
        #Trimming the list so that any places after an unoccupied place from the placed letters are removed.
        if len(r) >1:
            for j in range(r.index(i), 0, -1):
                if (r[j][1]-r[j-1][1]) > 1:

                    r=r[j:]
            for j in range(r.index(i), len(r), 1):
                try:
                    if (r[j+1][1] - r[j][1]) > 1:
                        r=r[:j+1]
                except:
                    pass
            wordsp.append(r)
            
        #Vertically
        pv = np.array(list(zip(list(range(0, 15, 1)), [i[1]] * 15)))[board[:, i[1]] < 52].tolist()
        s = []
        for k in pv:
            s.append(tuple(k))
        if len(s)>1:
            for j in range(r.index(i), 0, -1):
                if (r[j][0]-r[j-1][0]) > 1:

                    r=r[j:]
            for j in range(r.index(i), len(r), 1):
                try:
                    if (r[j+1][0] - r[j][0]) > 1:
                        r=r[:j+1]
                except:
                    pass
            wordsp.append(s)
    wordspq=[]
    for i in wordsp:
        wordspq.append(tuple(i))
        
    return list(set(wordspq))       # Set is used here to remove redundant words.

