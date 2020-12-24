with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

color_map = {}

for i in range(0, len(cases)):
    parsed_direction = []
    j = 0
    while (j < len(cases[i])):
        print(i, j, cases[i][j])
        if (cases[i][j] == 's' or cases[i][j] == 'n'):
            parsed_direction.append(cases[i][j] + cases[i][j+1])
            j = j + 1
        else:
            parsed_direction.append(cases[i][j])
        j = j+ 1
    cases[i] = parsed_direction

for i in range(0, len(cases)):
    starting_direction = [1,0]
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
    if(starting_direction in color_map): # and color_map[starting_direction] == "black"):
        color_map[starting_direction] += 1 # "white"
    else:
        color_map[starting_direction] = 1 # "black"

print(cases)
print(len(cases))
print(color_map)

print(len(color_map))
black = 0
white = 0
for key, value in color_map.items():
    if value % 2 == 1:
        black += 1
    else:
        white += 1

print(white)
print(black)