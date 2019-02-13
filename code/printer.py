import numpy as np
import platform


def printer(board):
    # covert board into a string array
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    board = np.array(board, dtype='<U2')  # convert dtype to string with 2 characters

    # set each of the elements to the appropriate alphabet (use a more efficient method?)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            board[i, j] = alphabet[int(board[i, j])]

    # check for installed libraries for colored output
    try:
        import termcolor
        if platform.system() == 'Windows':
            import colorama  # Needed on widows to convert byte sequences returned by termcolor into color
            colorama.init()
        color = True
    except ImportError:
        color = False

    # Color play (Recommended)
    if color:
        board2 = np.array(board, copy=True)
        special_words = np.array([' ' for x in range(15 * 15)], dtype='<U2')  # initialise an empty array
        special_words = special_words.reshape((15, 15))
        
        # coloringdict creates a dictionary for formatting functions to be used later
        coloringdict = {'TL': (lambda x: " " + termcolor.colored("   ", 'white', 'on_cyan') + " "),
                        'TW': (lambda x: " " + termcolor.colored("   ", 'white', 'on_red') + " "),
                        'DL': (lambda x: " " + termcolor.colored("   ", 'white', 'on_blue') + " "),
                        'DW': (lambda x: " " + termcolor.colored("   ", 'white', 'on_yellow') + " ")}
        for i in list([x for x in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")]):
            coloringdict[i] = lambda x: termcolor.colored(" ", 'red', 'on_magenta') + " " + x + " " + termcolor.colored(
                " ", 'red', 'on_magenta')
        coloringdict[' '] = lambda x: "     "
        
        # Set appropriate places on the board to the special words
        text = 'TW'
        special_words[np.array([0, 0, 0, 7, 7, 14, 14, 14]), np.array([0, 7, 14, 0, 14, 0, 7, 14])] = text
        text = 'DW'
        special_words[np.array([1, 1, 2, 2, 3, 3, 4, 4, 7, 10, 10, 11, 11, 12, 12, 13, 13]), np.array(
            [1, 13, 2, 12, 3, 11, 4, 10, 7, 4, 10, 3, 11, 2, 12, 1, 13])] = text
        text = 'TL'
        special_words[
            np.array([1, 1, 5, 5, 5, 5, 9, 9, 9, 9, 13, 13]), np.array([5, 9, 1, 5, 9, 13, 1, 5, 9, 13, 5, 9])] = text
        text = 'DL'
        special_words[
            np.array([0, 0, 2, 2, 3, 3, 3, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 11, 11, 11, 12, 12, 13, 13]), np.array(
                [3, 11, 6, 8, 0, 7, 14, 2, 6, 8, 12, 3, 11, 2, 6, 8, 12, 0, 7, 14, 6, 8, 3, 11])] = text
        board2[np.logical_and(board == ' ', special_words != ' ')] = special_words[
            np.logical_and(board == ' ', special_words != ' ')]  # Only the places where there are no tiles are replaced
            
        # Actual printing
        print("     |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |")
        print("  ----------------------------------------------------------------------------------------------")
        alph = list('abcdefghijklmno')
        for j in range(15):
            print("  " + alph[j] + "  |", end='')
            for i in range(15):
                print(coloringdict[board2[j][i]](board2[j][i]) + "|", end='')
            print("")
            print("  ----------------------------------------------------------------------------------------------")
            
        # Print legend
        print(termcolor.colored(" ", 'red', 'on_magenta') + ": Tile, ", end='')
        print(termcolor.colored(" ", 'red', 'on_red') + ": TW, ", end='')
        print(termcolor.colored(" ", 'red', 'on_yellow') + ": DW, ", end='')
        print(termcolor.colored(" ", 'red', 'on_cyan') + ": TL, ", end='')
        print(termcolor.colored(" ", 'red', 'on_blue') + ": DL, ")

    # Non-color play (not recommended)
    else:
        board2 = np.array(board, copy=True)
        special_words = np.array(['  ' for x in range(15 * 15)])
        special_words = special_words.reshape((15, 15))
        text = 'TW'
        special_words[np.array([0, 0, 0, 7, 7, 14, 14, 14]), np.array([0, 7, 14, 0, 14, 0, 7, 14])] = text
        text = 'DW'
        special_words[np.array([1, 1, 2, 2, 3, 3, 4, 4, 7, 10, 10, 11, 11, 12, 12, 13, 13]), np.array(
            [1, 13, 2, 12, 3, 11, 4, 10, 7, 4, 10, 3, 11, 2, 12, 1, 13])] = text
        text = 'TL'
        special_words[
            np.array([1, 1, 5, 5, 5, 5, 9, 9, 9, 9, 13, 13]), np.array([5, 9, 1, 5, 9, 13, 1, 5, 9, 13, 5, 9])] = text
        text = 'DL'
        special_words[
            np.array([0, 0, 2, 2, 3, 3, 3, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 11, 11, 11, 12, 12, 13, 13]), np.array(
                [3, 11, 6, 8, 0, 7, 14, 2, 6, 8, 12, 3, 11, 2, 6, 8, 12, 0, 7, 14, 6, 8, 3, 11])] = text
        board2[np.logical_and(board == '  ', special_words != '  ')] = special_words[
            np.logical_and(board == '  ', special_words != '  ')]
        text = '''
             |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |
          ----------------------------------------------------------------------------------------------
          a  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          b  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          c  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          d  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          e  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          f  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          g  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          h  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          i  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          j  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          k  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          l  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          m  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          n  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
          o  |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |  {} |
          ----------------------------------------------------------------------------------------------
        '''.format(*board2.flatten().tolist())
        print(text)
