#scorer
import string
import numpy as np

l=list(string.ascii_uppercase)
scoretile=[1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
letters_score=dict(zip(l,scoretile))

tw=[list(a) for a in zip([0, 0, 0, 7, 7, 14, 14, 14],[0, 7, 14, 0, 14, 0, 7, 14])]
dw=[list(a) for a in zip([1, 1, 2, 2, 3, 3, 4, 4, 7, 10, 10, 11, 11, 12, 12, 13, 13],[1, 13, 2, 12, 3, 11, 4, 10, 7, 4, 10, 3, 11, 2, 12, 1, 13])]
tl=[list(a) for a in zip([1, 1, 5, 5, 5, 5, 9, 9, 9, 9, 13, 13],[5, 9, 1, 5, 9, 13, 1, 5, 9, 13, 5, 9])]
dl=[list(a) for a in zip([0, 0, 2, 2, 3, 3, 3, 6, 6, 6, 6, 7, 7, 8, 8, 8, 8, 11, 11, 11, 12, 12, 13, 13],[3, 11, 6, 8, 0, 7, 14, 2, 6, 8, 12, 3, 11, 2, 6, 8, 12, 0, 7, 14, 6, 8, 3, 11])]

#words made in the move
def wordsmade(positions):
    pass

def scorer(letters,positions):
    wordsposition = wordsmade(positions)
    tempdict= dict(zip(positions,letters))
    score=[]
    for i in wordsposition:
        tilescores = 0
        newtiles=list(set(i).intersection(positions))
        for j in newtiles:
            if j in tl:
                tilescores=tilescores+((letters_score[tempdict[j]])*3)
            if j in dl:
                tilescores=tilescores+((letters_score[tempdict[j]])*2)
            else:
                tilescores=tilescores+(letters_score[tempdict[j]])
        for k in i:
            if k not in newtiles:
                tilescores=tilescores+(letters_score[numberletterkey[board[k[0]][k[1]]]])
        for j in newtiles:
            if j in  tw:
                tilescores=tilescores*3
            if j in dw:
                tilescores=tilescores*2
        score.append(tilescores)
    return sum(score)
