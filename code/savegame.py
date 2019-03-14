# Save game to file 'board.txt'

import numpy

# save board

numpy.savetxt('board.txt', board, fmt='%d', delimiter=',')

# load board

board = numpy.genfromtxt('board.txt', dtype=int, delimiter=',',
                         max_rows=15)

# save racks

with open('board.txt', 'a') as f:
    f.writelines(i for i in rack1)
    f.write('\n')
    f.writelines(i for i in rack2)
    f.write('\n')
    f.writelines(i for i in rack3)
    f.write('\n')
    f.writelines(i for i in rack4)
    f.write('\n')

# load racks

with open('board.txt', 'r') as f:
    for i in range(0, 15, 1):
        next(f)
    racklist = []
    for line in f:
        racklist.append(line[:-1])
rack1 = list(racklist[0])
rack2 = list(racklist[1])
rack3 = list(racklist[2])
rack4 = list(racklist[3])
