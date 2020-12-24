# Raw -> This can be refactored big time!
import copy

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

color_map = {}

for i in range(0, len(cases)):
    parsed_direction = []
    j = 0
    while (j < len(cases[i])):
        if (cases[i][j] == 's' or cases[i][j] == 'n'):
            parsed_direction.append(cases[i][j] + cases[i][j+1])
            j = j + 1
        else:
            parsed_direction.append(cases[i][j])
        j = j+ 1
    cases[i] = parsed_direction

for i in range(0, len(cases)):
    starting_direction = [0,0]
    for j in range(0, len(cases[i])):
        if cases[i][j] == "w":
            starting_direction[1] -= 1

        elif cases[i][j] == "e":
            starting_direction[1] += 1

        elif cases[i][j] == "nw":
            if(starting_direction[0] % 2 == 0):
                starting_direction[0] -= 1
                starting_direction[1] -= 1
            else:
                starting_direction[0] -= 1

        elif cases[i][j] == "ne":
            if(starting_direction[0] % 2 == 0):
                starting_direction[0] -= 1
            else:
                starting_direction[0] -= 1
                starting_direction[1] += 1

        elif cases[i][j] == "se":
            if(starting_direction[0] % 2 == 0):
                starting_direction[0] += 1
            else:
                starting_direction[0] += 1
                starting_direction[1] += 1


        elif cases[i][j] == "sw":
            if(starting_direction[0] % 2 == 0):
                starting_direction[0] += 1
                starting_direction[1] -= 1
            else:
                starting_direction[0] += 1

    starting_direction = tuple(starting_direction)
    if(starting_direction in color_map):
        color_map[starting_direction] += 1
    else:
        color_map[starting_direction] = 1

day = 1
target_day = 100

even_adjacents = [
    (-1, -1),
    (-1, 0),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
]

odd_adjacents = [
    (-1,0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, 0),
    (1, 1),
]

def count_black(color_map):
    white, black = 0,0
    for key, value in color_map.items():
        if value % 2 == 1:
            black += 1
        else:
            white += 1
    return black

print('Day 0 -', count_black(color_map))
while (day <= target_day):
    neighbours = []
    for key, value in color_map.items():
        if(key[0] % 2 == 0):
            adjacents = even_adjacents[:]
        else:
            adjacents = odd_adjacents[:]

        neighbours.append(key)
        for adjacent in adjacents:
            neighbours.append((key[0] + adjacent[0], key[1] + adjacent[1]))

    new_color_map = {}
    for tile in neighbours:
        if(tile[0] % 2 == 0):
            adjacents = even_adjacents[:]
        else:
            adjacents = odd_adjacents[:]

        black_tiled_neighbours = 0
        for adjacent in adjacents:
            row = tile[0] + adjacent[0]
            column = tile[1] + adjacent[1]

            if ((row,column) in color_map and color_map[(row, column)] % 2 == 1):
                black_tiled_neighbours += 1

        if(tile in color_map and color_map[tile] % 2 == 1 and black_tiled_neighbours in [1,2]):
            new_color_map[tile] = 1
        elif((not tile in color_map) or color_map[tile] % 2 == 0):
            if(black_tiled_neighbours == 2):
                new_color_map[tile] = 1

    color_map = copy.copy(new_color_map)
    print(f'Day {day} - {count_black(color_map)}')
    day += 1
