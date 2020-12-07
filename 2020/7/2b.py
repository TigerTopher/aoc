with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

# Passing multiplier instead of multiplying outside
def getBagCount(initialColor, multiplier):
    bagCount = 1

    for rule in cases:
        rule = rule.split(' bags contain ')
        leftColor = rule[0]
        rightColor = rule[1]
        
        if (initialColor == leftColor):
            if(rightColor == "no other bags."):
                return multiplier*1

            genColorProcessed = rightColor.split(', ')
            for color in genColorProcessed:
                currentBagCount = int(color.split(' ')[0])
                bagColor = ' '.join(color.split(' ')[1:-1])
                bagCount = bagCount + getBagCount(bagColor, currentBagCount)

    return multiplier*bagCount

output = getBagCount('shiny gold', 1) - 1 # Subtract the initial shiny gold bag
print(output)
