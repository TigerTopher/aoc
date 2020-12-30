import copy

with open('input') as f:
    raw_tiles = "".join(f.readlines()).rstrip('\n').split("\n\n")

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


tiles = []
match_count = 0

for raw_tile in raw_tiles:
    tile_number, tile = raw_tile.lstrip('Tile: ').split(':\n')
    tile = tile.split("\n")
    for i in range(0, len(tile)):
        tile[i] = list(tile[i])
    tile = Tile(tile_number, tile)
    tiles.append(tile)

board = [tiles.pop(0)]

def matchSides(current_tile, board_tile):
    matched = False
    if(current_tile.getBottom() == board_tile.getTop()):
        board_tile.top = current_tile
        current_tile.bottom = board_tile
        matched = True
        # print("Matched bottom")
    if(current_tile.getTop() == board_tile.getBottom()):
        board_tile.bottom = current_tile
        current_tile.top = board_tile
        matched = True
        # print("Matched top")

    if(current_tile.getLeft() == board_tile.getRight()):
        board_tile.right = current_tile
        current_tile.left = board_tile
        matched = True
        # print("Matched left")

    if(current_tile.getRight() == board_tile.getLeft()):
        board_tile.left = current_tile
        current_tile.right = board_tile
        matched = True
        # print("Matched right")

    if(matched):
        # print("Matched: ", current_tile.number, board_tile.number)
        return True
    return False

def findMatch(current_tile):
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

def findMatchAll(current_tile):
    matchFound = False

    for board_tile in board:
        if(current_tile.number != board_tile.number):
            if (matchSides(current_tile, board_tile)):
                matchFound = True
    return matchFound

totalCount = len(tiles)
i = 0
while (tiles != []):
    current_tile = tiles.pop(0)
    if not findMatch(current_tile):
        tiles.append(current_tile)
    else:
        board.append(current_tile)
    i += 1

for board_tile in board:
    findMatchAll(board_tile)

start = board[0]
while(start.left != next):
    start = start.left

while(start.top != next):
    start = start.top

tiles = []
tile = []
while(start != next):
    tile = []
    while(start != next):
        tile.append(start)
        start = start.right
    start = tile[0]
    tiles.append(tile)
    start = start.bottom

# Build the solution
solution_grid = []

for tile_row in tiles:
    for i in range(1, 9):
        solution_row = []
        for tile in tile_row:
            solution_row += tile.value[i][1:-1]
        solution_grid.append(solution_row)

solution_grid_row = len(solution_grid)
solution_grid_column = len(solution_grid[0])

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

# 120 x 120
# 15 - #s
monster = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]
]

# monster = [
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
#     ['#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '#'],
#     ['.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '.', '.', '.']
# ]

def f(s):
    pass

wildSea = 0
for grid in solution_grid:
    for element in grid:
        if element == '#':
            wildSea += 1

monsterFound = 0
for angle in [0, 90, 90, 90]:
    for operation in [f, flipVertical, flipHorizontal]:
        solution_grid = rotateClockwise(angle, solution_grid)
        operation(solution_grid)
        for i in range(0, solution_grid_row-2):
            for j in range(0, solution_grid_column-19):
                subsets = solution_grid[i:i+3]
                for k in range(0, len(subsets)):
                    subsets[k] = subsets[k][j:j+20]
                match = True
                for k in range(0, 3):
                    for l in range(0, 20):
                        if(monster[k][l] and subsets[k][l] != '#'):
                            match = False
                if(match):
                    monsterFound += 1
        if(monsterFound != 0):
            print('Monster found:', monsterFound)
            print('Wild Sea:', wildSea)
            print('#s that are not part of sea monster:', wildSea - (monsterFound*15))
            exit()
        operation(solution_grid)
