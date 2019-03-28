# input output

print('Welcome to the game of SCRABBLE!')
print('Would you like to play?')
if input('yes or no? ').lower() == 'no':
    exit()
else:
    print('Do you want to play a new game or load a saved game?')
    status = input('Enter new or old: ')
    if status == 'new':
        while True:  # Loops until a valid number of players is entered
            n = int(input('Enter the number of players: '))
            if (n < 2) or (n > 4):
                print('This game can only be played by 2-4 players.')
            else:
                break
        playernames = []
        for i in range(n):
            playernames.append(input('Enter the name of player ' + str(i) + ': '))
        currentgame = GameEngine(playernames, 'new')
        cont = False  # A bool allowing to decide for continuing based on the validity of the enetered move
        while not cont:
            printer(currentgame.board)
            for i in currentgame.players:
                print(i.name, ': Your score is ', i.score)
            print(playernames[currentgame.turn], ', it is your turn. Here are the letters in you rack.')
            print(currentgame.players[currentgame.turn].rack)
            print('Type the word you want to place on the board. This should contain all the new tiles you are adding.')
            print('Enter all non-blank tiles as capitals \
            and any blank tiles using the small letter of the letter you want to use the blank tile as.')
            playerinput = []
            playerinput.append(str(input('Word to be played: ')))
            print('Where is the first letter of the word you made on the board?')
            playerinput.append([int(input('Enter the row number here: ')), int(input('Enter the column number here: '))])
            print('Is your word vertically placed or horizontally placed?')
            playerinput.append(str(input('Enter v or h here: ')))
            if currentgame.scrabbleit(playerinput):
                cont = True
                reply = input('Enter Q to quit without saving, S to save the game and anything else to continue: ')
                if reply == 'S':
                    currentgame.save(filename=input('Enter the name of the saved file (press enter to use the default): '))
                elif reply == 'Q':
                    exit()
            else:
                print('The word/indices you entered was invalid. Please enter again.')
