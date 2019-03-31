# input output
from GameEngine import GameEngine
from printer import printer

scores = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]


def rules():
    inp = input('Do you want to read the rules? y/n: ').lower()
    if inp == 'n':
        return
    with open('rules.txt') as f:
        for line in f:
            input(line.split('\n')[0])


print('Welcome to the game of SCRABBLE!')
print('')
print('Would you like to play?')
if input('yes or no?: ').lower() == 'no':
    exit()
else:
    rules()
    print('Do you want to play a new game or load a saved game?')
    status = input('Enter new or old: ').lower()
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
        inp = input("Disable validity mode (forces all words to be checked against a wordlist) (y/n): ").lower()
        if inp != 'y':
            filename = input("Enter the path to a wordlist file. \nKeep empty for the default SOWPODS(format: new words on each new line, no capitals): ")
            if filename == '':
                currentgame = GameEngine(playernames, 'new')
            else:
                currentgame = GameEngine(playernames, 'new', filename=filename)
        else:
            currentgame = GameEngine(playernames, 'new', False)
    elif status == 'old':
        savefilename = input('Enter the path of the saved file (press enter for default): ')
        inp = input("Disable validity mode (forces all words to be checked against a wordlist) (y/n): ").lower()
        if inp != 'y':
            filename = input(
                "Enter the path to a wordlist file. \nKeep empty for the default SOWPODS(format: new words on each new line, no capitals): ")
            if filename == '':
                filename = 'wordlist/sowpods.txt'
            if savefilename == '':
                currentgame = GameEngine(gamestatus='old', validity_mode=True, filename=filename)
            else:
                currentgame = GameEngine(gamestatus='old', validity_mode=True, filename=filename,
                                         savefilename=savefilename)
        else:
            if savefilename == '':
                currentgame = GameEngine(gamestatus='old', validity_mode=False)
            else:
                currentgame = GameEngine(gamestatus='old', validity_mode=False, savefilename=savefilename)

    reply = 'C'
    while reply == 'C':
        cont = False  # A bool allowing to decide for continuing based on the validity of the enetered move
        while not cont:
            printer(currentgame.board)
            for i in currentgame.players:
                print(i.name, ': Your score is ', i.score)
            print(currentgame.players[currentgame.turn].name, ', it is your turn. Here are the letters in you rack.')
            print(currentgame.players[currentgame.turn].rack)
            inp = input('Do you want to exchange tiles - y/n? (Only possible if the tiles in the pouch are more than 7): ').lower()
            if inp=='y':
                tiles_to_exchange = input('Enter the tiles you want to exchange (enter a space to exchange a blank tile) - \nexample (ABC to exchange A, B and C): ')
                tiles_to_exchange = list(tiles_to_exchange)
                status = currentgame.exchange(tiles_to_exchange)
                if status[0]:
                    input('Successfully exchanged. Press enter to continue.')
                    continue
                else:
                    print(status[1])
                    input('Unsuccessful exchange. Press enter to continue.')
                    continue
            print('Tile Scores: ' + ''.join([' '+list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[x] + '=' + str(scores[x]) + ' ' for x in range(len(scores))]))
            print('Type the word you want to place on the board. This should contain all the new tiles you are adding.')
            print('Enter all non-blank tiles as capitals and any blank tiles using the \nsmall letter of the letter you want to use the blank tile as.')
            playerinput = []
            playerinput.append(str(input('Word to be played: ')))
            print('Where is the first letter of the word you made on the board?')
            playerinput.append(
                [int(input('Enter the row number here: ')), int(input('Enter the column number here: '))])
            print('Is your word vertically placed or horizontally placed?')
            playerinput.append(str(input('Enter v or h here: ')).lower())
            scrabbleit = currentgame.scrabbleit(playerinput)
            if scrabbleit[0]:
                cont = True
                reply = input('Enter Q to quit without saving, S to save the game and quit, and anything else to continue: ')
                if reply == 'S':
                    filename = input('Enter the name of the saved file (press enter to use the default): ')
                    if filename != '':
                        currentgame.save(filename=filename)
                    else:
                        currentgame.save()
                    exit()
                elif reply == 'Q':
                    exit()
                else:
                    reply = 'C'
                    if scrabbleit[1]:
                        reply = 'E'
            else:
                print(scrabbleit[1])
                input('The input you entered was invalid. Please enter again.')

    if reply == 'E':
        print('The game has ended! Here are your scores: ')
        for i in currentgame.players:
            print(i.name, ': Your score is ', i.score)
            finalscores = list(x.score for x in currentgame.players)
            winner = currentgame.players[finalscores.index(max(finalscores))].name
            input()
        print('The winner is: ', winner)
        print('!!!!!! Congratulations !!!!!!')
        print('Game credits @FlyingFordAnglia, @Stochastic13')
        input()
