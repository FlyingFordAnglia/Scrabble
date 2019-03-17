
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
