with open('input') as f:
    map_config = [line.rstrip() for line in f.readlines()]

def get_trees(right, down):
    horizontal_limit = len(map_config[0])
    i = horizontal = trees = 0

    while i < len(map_config):
        if(map_config[i][horizontal] == "#" and i != 0):
            trees += 1

        horizontal = (horizontal + right) % horizontal_limit
        i = i + down

    return trees

print(get_trees(3,1))