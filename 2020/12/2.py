with open('input') as f:
    instructions = [line.rstrip() for line in f.readlines()]

def getManhattanDistance(x, y):
    return abs(x) + abs(y)

def rotate(coordinates, units, action):
    steps = (units // 90) % 4
    for i in range(0, steps):
        if(action == "R"):
            coordinates['waypoint_x'] *= -1
        elif(action == "L"):
            coordinates['waypoint_y'] *= -1
        coordinates['waypoint_x'], coordinates['waypoint_y'] = coordinates['waypoint_y'], coordinates['waypoint_x']

    return coordinates

def move(coordinates, units):
    coordinates['y'] = coordinates['y'] + (units* coordinates['waypoint_y'])
    coordinates['x'] = coordinates['x'] + (units* coordinates['waypoint_x'])
    return coordinates

def moveWayPoint(coordinates, units, action):
    if(action == "W"):
        coordinates['waypoint_x'] -= units
    elif(action == "N"):
        coordinates['waypoint_y'] += units
    elif(action == "S"):
        coordinates['waypoint_y'] -= units
    elif(action == "E"):
        coordinates['waypoint_x'] += units

    return coordinates

coordinates = {
    'x': 0,
    'y': 0,
    'waypoint_x': 10,
    'waypoint_y': 1
}

directions = list('NSWE')
rotations = list('LR')

for i in instructions:
    action = i[0]
    units = int(i[1:])

    print(i)
    if(action == "F"):
        coordinates = move(coordinates, units)
        print(" -> Moved to", coordinates['x'], "E", coordinates['y'], "N")

    if(action in directions):
        coordinates = moveWayPoint(coordinates, units, action)
        print(" -> Moved waypoint to", coordinates['waypoint_x'], "E", coordinates['waypoint_y'], "N")
    
    if(action in rotations):
        coordinates = rotate(coordinates, units, action)
        print(" -> Rotated waypoint to", coordinates['waypoint_x'], "E", coordinates['waypoint_y'], "N")

print(coordinates['x'], coordinates['y'], getManhattanDistance(coordinates['x'], coordinates['y']))
