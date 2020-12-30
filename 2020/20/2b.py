class Tile:
    def __init__(self, number, value=[[]], left=next, right=next, top=next, bottom=next):
        self.number = int(number)
        self.value = value

        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def getTop(self):
        return self.value[0]

    def getLeft(self):
        return [i[0] for i in self.value]

    def getRight(self):
        return [i[-1] for i in self.value]

    def getBottom(self):
        return self.value[-1]

    def __repr__(self):
        return str(self.number)
    
    def print(self):
        print(str('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in self.value])))

    def rotateClockwise(self, target_angle):
        current_angle = 0
        while(current_angle < target_angle):
            list_of_tuples = zip(*self.value[::-1])
            self.value = [list(elem) for elem in list_of_tuples]
            current_angle += 90

    def flipVertical(self):
        self.value.reverse()

    def flipHorizontal(self):
        for i in range(0, len(self.value)):
            self.value[i].reverse()

def matchSides(current_tile, board_tile):
    if(current_tile.getBottom() == board_tile.getTop()):
        board_tile.top = current_tile
        current_tile.bottom = board_tile
        return True
    if(current_tile.getTop() == board_tile.getBottom()):
        board_tile.bottom = current_tile
        current_tile.top = board_tile
        return True
    if(current_tile.getLeft() == board_tile.getRight()):
        board_tile.right = current_tile
        current_tile.left = board_tile
        return True
    if(current_tile.getRight() == board_tile.getLeft()):
        board_tile.left = current_tile
        current_tile.right = board_tile
        return True

    return False

def flipVertical(array):
    array.reverse()

def flipHorizontal(array):
    for i in range(0, len(array)):
        array[i].reverse()

def rotateClockwise(target_angle, array):
    current_angle = 0
    while(current_angle < target_angle):
        list_of_tuples = zip(*array[::-1])
        array = [list(elem) for elem in list_of_tuples]
        current_angle += 90
    return array

def findMatch(current_tile, board):
    matchFound = False
    for board_tile in board:
        for angle in [0, 90, 90, 90]:
            current_tile.rotateClockwise(angle)
            if (matchSides(current_tile, board_tile)):
                return True

            current_tile.flipVertical()
            if (matchSides(current_tile, board_tile)):
                return True
                
            current_tile.flipVertical()
            current_tile.flipHorizontal()

            if (matchSides(current_tile, board_tile)):
                return True
            current_tile.flipHorizontal()
        current_tile.rotateClockwise(90)
    return matchFound

def findMatchAll(current_tile, board):
    matchFound = False

    for board_tile in board:
        if(current_tile.number != board_tile.number):
            if (matchSides(current_tile, board_tile)):
                matchFound = True
    return matchFound

def connectAllTiles(unprocessed_tiles):
    board = [unprocessed_tiles.pop(0)]
    while (unprocessed_tiles != []):
        current_tile = unprocessed_tiles.pop(0)
        if not findMatch(current_tile, board):
            unprocessed_tiles.append(current_tile)
        else:
            board.append(current_tile)

    for board_tile in board:
        findMatchAll(board_tile, board)
    return board

def buildSolutionGrid(board):
    start = board[0]
    while(start.left != next):
        start = start.left

    while(start.top != next):
        start = start.top

    tiles = []
    while(start != next):
        tile = []
        while(start != next):
            tile.append(start)
            start = start.right
        start = tile[0]
        tiles.append(tile)
        start = start.bottom

    solution_grid = []

    # Changing range to (1,9) and [1:-1] trims the border
    for tile_row in tiles:
        for i in range(1, 9):
            solution_row = []
            for tile in tile_row:
                solution_row += tile.value[i][1:-1]
            solution_grid.append(solution_row)

    return solution_grid

def nop(*args):
    pass

def getWildSeaCount(solution_grid):
    return sum([row.count('#') for row in solution_grid])

def getMonsterCount(solution_grid):
    monsterFound = 0
    monster = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]

    solution_grid_row = len(solution_grid)
    solution_grid_column = len(solution_grid[0])
    monster_grid_row = len(monster)
    monster_grid_column = len(monster[0])

    for angle in [0, 90, 90, 90]:
        for operation in [nop, flipVertical, flipHorizontal]:
            solution_grid = rotateClockwise(angle, solution_grid)
            operation(solution_grid)
            for i in range(0, solution_grid_row - monster_grid_row + 1):
                for j in range(0, solution_grid_column - monster_grid_column + 1):
                    subsets = solution_grid[i:i+monster_grid_row]
                    for k in range(0, len(subsets)):
                        subsets[k] = subsets[k][j:j+monster_grid_column]
                    match = True
                    for k in range(0, monster_grid_row):
                        for l in range(0, monster_grid_column):
                            if(monster[k][l] and subsets[k][l] != '#'):
                                match = False
                    if(match):
                        monsterFound += 1
            if(monsterFound != 0):
                return monsterFound
            operation(solution_grid)

def countNotPartOfSeaMonster(wildSea, monsterCount):
    return wildSea - (monsterCount*15)  # Monster has 15 #s that are not part of wild sea

def parseTiles():
    with open('input') as f:
        raw_tiles = "".join(f.readlines()).rstrip('\n').split("\n\n")

    unprocessed_tiles = []

    for raw_tile in raw_tiles:
        tile_number, tile = raw_tile.lstrip('Tile: ').split(':\n')
        tile = list(map(list, tile.split("\n")))
        tile = Tile(tile_number, tile)
        unprocessed_tiles.append(tile)
    
    return unprocessed_tiles

def main():
    unprocessed_tiles = parseTiles()
    board = connectAllTiles(unprocessed_tiles)
    solution_grid = buildSolutionGrid(board)
    print(solution_grid)
    wildSea = getWildSeaCount(solution_grid)
    monsterCount = getMonsterCount(solution_grid)

    print('Monster found:', monsterCount)
    print('Wild Sea:', wildSea)
    print('#s that are not part of sea monster:', countNotPartOfSeaMonster(wildSea, monsterCount))

if __name__ == "__main__":
    main()
