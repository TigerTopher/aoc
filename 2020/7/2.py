with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

def getBagCount(initialColor):
    bagCount = 1

    for rule in cases:
        rule = rule.split(' bags contain ')
        leftColor = rule[0]
        rightColor = rule[1]
        
        if (initialColor == leftColor):
            # Base case
            if(rightColor == "no other bags."):
                return 1

            genColorProcessed = rightColor.split(', ')

            for color in genColorProcessed:
                currentBagCount = int(color.split(' ')[0])
                bagColor = ' '.join(color.split(' ')[1:-1])

                bagCount = bagCount + currentBagCount*getBagCount(bagColor)

    return bagCount

output = getBagCount('shiny gold') - 1 # Subtract the initial shiny gold bag
print(output)
