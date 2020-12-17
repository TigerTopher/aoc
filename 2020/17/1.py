import math

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

active_cubes = set()

for x in range(0, len(cases)):
    for y in range(0, len(cases[x])):
        if(cases[x][y] == '#'):
            active_cubes.add((x,y,0))

cycle = 0
while(cycle < 6):
    next_active_cubes = set()
    for active_cube in active_cubes:
        neighbours = []
        for x in [-1,0,1]:
            for y in [-1,0,1]:
                for z in [-1,0,1]:
                    neighbours.append((active_cube[0] + x, active_cube[1] + y, active_cube[2] + z))

        for cube in neighbours:            
            active_neighbours = 0
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    for z in [-1,0,1]:
                        if(not(x==y==z==0)):
                            if( (cube[0]+x, cube[1]+y, cube[2]+z) in active_cubes):
                                active_neighbours += 1
            if(cube in active_cubes and active_neighbours in [2,3]):
                next_active_cubes.add(cube)
            if(not cube in active_cubes and active_neighbours == 3):
                next_active_cubes.add(cube)

    cycle += 1
    active_cubes = next_active_cubes

print(len(next_active_cubes))
