with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

graph = {}

# Looping once through the input to build the graph. 
for case in cases:
    break_down = case.split(" bags contain ")
    leftColor = break_down[0]
    rightColors = break_down[1].split(", ")
    for i in range(0, len(rightColors)):
        rightColors[i] = ' '.join(rightColors[i].split(' ')[1:-1])
    
    for rightColor in rightColors:
        if(rightColor in graph):
            graph[rightColor].append(leftColor)
        else:
            graph[rightColor] = [leftColor]

colors = []

# Iterate Graph
def iterateParentBag(color, delimiter):
    global colors
    global graph

    print(delimiter, color)
    if(not color in graph):
        return
    colors += graph[color]
    for color in graph[color]:
        iterateParentBag(color, '-' + delimiter)

iterateParentBag('shiny gold', '>')
print(len(set(colors)))
