with open('input') as f:
    raw_tiles = "".join(f.readlines()).rstrip('\n').split("\n\n")

tiles = []
for i in range(0, len(raw_tiles)):
    tile_number, tile = raw_tiles[i].lstrip('Tile: ').split(':\n')
    tile = tile.split('\n')
    tiles.append({
        'number': int(tile_number),
        'top': tile[0],
        'left': ''.join([i[0] for i in tile]),
        'right': ''.join([i[-1] for i in tile]),
        'bottom': tile[-1],
    })

orientations = ['left', 'top', 'right', 'bottom']
product = 1
for i in range(0, len(tiles)):
    matches = {
        'left': 0,
        'top': 0,
        'right': 0,
        'bottom': 0
    }
    for j in range(0, len(tiles)):
        if i == j:
            continue
        for orientation1 in orientations:
            for orientation2 in orientations:
                matches[orientation1] += tiles[i][orientation1] == tiles[j][orientation2]
                matches[orientation1] += tiles[i][orientation1] == tiles[j][orientation2][::-1]
                matches[orientation1] += tiles[i][orientation1][::-1] == tiles[j][orientation2]
                matches[orientation1] += tiles[i][orientation1][::-1] == tiles[j][orientation2][::-1]

    # Idea: If at least two sides don't find a match, then it's a corner!
    if(list(matches.values()).count(0) == 2): 
        product *= tiles[i]['number']

print(product)
