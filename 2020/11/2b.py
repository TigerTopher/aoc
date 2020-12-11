import copy

with open('input') as f:
    cases = [list(line.rstrip()) for line in f.readlines()]

def getOccupiedCount(seatMatrix, char="#"):
    return sum([i.count(char) for i in seatMatrix])

def countVisiblyAdjacent(seatMatrix, i, j):
    visiblyAdjacentSeats, rows, columns = 0, len(seatMatrix), len(seatMatrix[0])
    for row_factor in [-1, 0, 1]:
        for column_factor in [-1, 0, 1]:
            if( not (row_factor == column_factor == 0)):
                k, l = i + row_factor, j + column_factor
                while ( k >= 0 and l >= 0 and k < rows and l < columns):
                    if(seatMatrix[k][l] == "L"): break
                    if(seatMatrix[k][l] == "#"):
                        visiblyAdjacentSeats += 1
                        break
                    k, l = k + row_factor, l + column_factor
    return visiblyAdjacentSeats

def performTransformations(seatMatrix, findSymbol, replaceSymbol, isValidAdjacentCount):
    boardCopy = copy.deepcopy(seatMatrix)
    for i in range(0, len(seatMatrix)):
        for j in range(0, len(seatMatrix[i])):
            adjacentSeats = countVisiblyAdjacent(boardCopy, i, j)
            if(boardCopy[i][j] == findSymbol and isValidAdjacentCount(adjacentSeats)) : seatMatrix[i][j] = replaceSymbol
    return getOccupiedCount(seatMatrix) if boardCopy == seatMatrix else 0

while True:
    count = performTransformations(cases, 'L', '#', (lambda adjacentSeats: adjacentSeats == 0)) or performTransformations(cases, '#', 'L', (lambda adjacentSeats: adjacentSeats >= 5))
    if(count): [print(count), exit()]
