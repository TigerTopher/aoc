# First attempt
import copy

with open('input') as f:
    cases = [list(line.rstrip()) for line in f.readlines()]

while True:
    boardCopy = copy.deepcopy(cases)

    for i in range(0, len(cases)):
        for j in range(0, len(cases[i])):
            adjacentSeats = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if(not (k == l == 0) and (i+k >= 0) and (j+l >= 0)):
                        try:
                            if(boardCopy[i+k][j+l] == '#'):
                                adjacentSeats += 1
                        except:
                            pass

            if(boardCopy[i][j] == 'L' and adjacentSeats == 0):
                cases[i][j] = '#'

    boardCopy = copy.deepcopy(cases)
    for i in range(0, len(cases)):
        for j in range(0, len(cases[i])):
            adjacentSeats = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if(not (k == l == 0) and (i+k >= 0) and (j+l >= 0)):
                        try:
                            if(boardCopy[i+k][j+l] == '#'):
                                adjacentSeats += 1
                        except:
                            pass
            if(boardCopy[i][j] == '#' and adjacentSeats >= 4):
                cases[i][j] = 'L'

    count = 0
    for i in range(0, len(cases)):
        count += cases[i].count('#')
    print(count)
