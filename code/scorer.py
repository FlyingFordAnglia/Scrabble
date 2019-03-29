import string

scoretile = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
letters_score = dict(zip(list(string.ascii_uppercase), scoretile))
for i in list(string.ascii_lowercase):
    letters_score[i] = 0

l_1 = dict(zip(list(range(0, 26, 1)), string.ascii_uppercase))
l_2 = dict(zip(list(range(26, 52, 1)), string.ascii_lowercase))
numberletterkey = {**l_1, **l_2}
numberletterkey[52] = ' '

tw = [list(a) for a in zip([0, 0, 0, 7, 7, 14, 14, 14], [0, 7, 14, 0, 14, 0, 7, 14])]
dw = [list(a) for a in zip([1, 1, 2, 2, 3, 3, 4, 4, 7, 10, 10, 11, 11, 12, 12, 13, 13],
                           [1, 13, 2, 12, 3, 11, 4, 10, 7, 4, 10, 3, 11, 2, 12, 1, 13])]
tl = [list(a) for a in zip([1, 1, 5, 5, 5, 5, 9, 9, 9, 9, 13, 13], [5, 9, 1, 5, 9, 13, 1, 5, 9, 13, 5, 9])]
dl = [list(a) for a in zip([0, 0, 2, 2, 3, 3, 3, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 11, 11, 11, 12, 12, 13, 13],
                           [3, 11, 6, 8, 0, 7, 14, 2, 6, 8, 12, 3, 11, 2, 6, 8, 12, 0, 7, 14, 6, 8, 3, 11])]


def scorer(move, wordsposition, board):
    letters = move[0]
    positions = list(map(tuple, move[1]))
    tempdict = dict(zip(positions, letters))
    score = 0
    for i in wordsposition:
        tilescores = 0
        newtiles = set(i).intersection(set(positions))
        for j in newtiles:
            if j in tl:
                tilescores = tilescores + ((letters_score[tempdict[j]]) * 3)
            elif j in dl:
                tilescores = tilescores + ((letters_score[tempdict[j]]) * 2)
            else:
                tilescores = tilescores + (letters_score[tempdict[j]])
        for j in (set(i) - set(positions)):
            tilescores = tilescores + (letters_score[numberletterkey[board[j[0]][j[1]]]])
        for j in newtiles:
            if j in tw:
                tilescores = tilescores * 3
            if j in dw:
                tilescores = tilescores * 2
        score += tilescores
    return score

def endscore(players,turn):
    remaining_players=players.pop(turn)
    for i in remaining_players:
        last_score=0
        for j in i.rack:
            last_score+=letters_score[j]
            i.score=i.score-letters_score[j]
        players[turn].score+=last_score
