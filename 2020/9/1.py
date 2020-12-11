import math

with open('input') as f:
    cases = [int(line.rstrip()) for line in f.readlines()]

def checkValid(i, lastRange):
    global cases
    default = False
    last25 = cases[i-lastRange:i]
    for j in range(0, len(last25)):
        for k in range(0, len(last25)):
            if (j != k):
                if((last25[j] + last25[k] == cases[i]) and (last25[j] != last25[k])):
                    default = True
    return default

missingNumber = 0
for i in range(25, len(cases)):
    if(not checkValid(i, 25)):
        missingNumber = cases[i]
        # Part 1 answer:
        print(cases[i])
        break
