"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.

Multiply all the trees
"""

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

print(get_trees(3,1) * get_trees(1,1) * get_trees(5,1) * get_trees(7,1) * get_trees(1,2))