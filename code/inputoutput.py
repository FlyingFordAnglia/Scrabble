# input output


print('Welcome to the game of Scrabble!!')
print('Would you like to play?')
if input('yes or no?') is 'no':
    exit()
else:
    print('Do you want to play a new game or load a saved game?')
    status = input('Enter new or old')
    if status == 'new':
        player
        names = str(input('Enter player names here.\
         Format: \'playername1,playername2,playername3,playername4\' ')).split(',')
        if len(playernames) < 2:
            print('This game requires a minimum of two players.')
            playernames = str(input('Enter player names here. \
            Format: \'playername1,playername2,playername3,playername4\' ')).split(',')

        currentgame = GameEngine(playernames, 'new')
        printer(currentgame.board)

        cont = False
        while not cont:
            printer(currentgame.board)
            for i in currentgame.players:
                print(i.name, ': Your score is ', i.score)
            print(playernames[currentgame.turn], ', it is your turn. Here are the letters in you rack.')
            print(currentgame.players[currentgame.turn].rack)
            print('Type the word you want to place on the board.')
            print('Enter all non-blank tiles as capitals \
            and any blank tiles using the small letter of the letter you want to use the blank tile as.')
            playerinput = []
            playerinput.append(str(input('Enter the word here.')))
            print('Where is the first letter of the word you made on the board?')
            playerinput.append([int(input('Enter the row number here.')), int(input('Enter the column number here'))])
            print('Is your word vertically placed or horizontally placed?')
            playerinput.append(str(input('Enter v or h here.')))
            playerinput.append(currentgame.turn)
            if currentgame.scrabbleit(playerinput):
                cont = True
                continue
            else:
                print('The word you entered was invalid. Please enter again.')
