import math

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

colors = []
def iterateBags(initialColor):
    for rule in cases:
        rule = rule.split(' bags contain ')
        newColor = rule[0]
        genColor = rule[1]
        if(initialColor in genColor):
            iterateBags(newColor)
            if(not newColor in colors):
                colors.append(newColor)

iterateBags('shiny gold')

print(len(colors))
