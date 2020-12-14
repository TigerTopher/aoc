with open('input') as f:
    instructions = [line.rstrip() for line in f.readlines()]

def getManhattanDistance(x, y):
    return abs(x) + abs(y)

def rotate(direction, action, units):
    directions = {
        "E": 0,
        "N": 90,
        "W": 180,
        "S": 270,
    }

    if(units == 0):
        return direction
    elif(action == "L"):
        return (direction + units) % 360
    elif(action == "R"):
        return (direction - units) % 360

def move(action, direction, units, vertical_axis, horizontal_axis):
    directions = {
        0: "E",
        90: "N",
        180: "W",
        270: "S",
    }

    if(action == "F"):
        action = directions[direction]

    if(action == "W"):
        horizontal_axis -= units
    elif(action == "N"):
        vertical_axis += units
    elif(action == "S"):
        vertical_axis -= units
    elif(action == "E"):
        horizontal_axis += units

    return [vertical_axis, horizontal_axis]

# ............
direction = 0
vertical_axis = 0
horizontal_axis = 0

directions = list('NSWEF')
rotations = list('LR')

for i in instructions:
    action = i[0]
    units = int(i[1:])

    print(i)
    if(action in directions):
        newCoordinates = move(action, direction, units, vertical_axis, horizontal_axis)
        vertical_axis = newCoordinates[0]
        horizontal_axis = newCoordinates[1]
        print(" -> Moved to", horizontal_axis, "E", vertical_axis, "N")
    
    if(action in rotations):
        direction = rotate(direction, action, units)
        print(" -> Rotated to", direction)
print(vertical_axis, horizontal_axis, getManhattanDistance(vertical_axis, horizontal_axis))
