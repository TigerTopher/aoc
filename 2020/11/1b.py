# Refactored
import copy

with open('input') as f:
    cases = [list(line.rstrip()) for line in f.readlines()]

def getOccupiedCount(seatMatrix, char="#"):
    return sum([i.count(char) for i in seatMatrix])

def countAdjacentSeats(seatMatrix, i, j, adjacentSeatSymbol = '#'):
    adjacentSeats, rows, columns = 0, len(seatMatrix), len(seatMatrix[0])
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if(not (k == l == 0) and (i+k >= 0) and (j+l >= 0) and (i+k < rows) and (j+l < columns) ):
                if(seatMatrix[i+k][j+l] == adjacentSeatSymbol):
                    adjacentSeats += 1
    return adjacentSeats

def performTransformations(seatMatrix, findSymbol, replaceSymbol, isValidAdjacentCount):
    boardCopy = copy.deepcopy(seatMatrix)
    for i in range(0, len(seatMatrix)):
        for j in range(0, len(seatMatrix[i])):
            adjacentSeats = countAdjacentSeats(boardCopy, i, j)
            if(boardCopy[i][j] == findSymbol and isValidAdjacentCount(adjacentSeats)):
                seatMatrix[i][j] = replaceSymbol

    return getOccupiedCount(seatMatrix) if boardCopy == seatMatrix else 0

while True:
    count = performTransformations(cases, 'L', '#', (lambda adjacentSeats: adjacentSeats == 0)) or performTransformations(cases, '#', 'L', (lambda adjacentSeats: adjacentSeats >= 4))
    if(count):
        print(count)
        exit()
