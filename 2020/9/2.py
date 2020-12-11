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

def findNumberSet(missingNumber):
    global cases
    for j in range(2, len(cases)):
        for k in range(0, len(cases) - j):
            if(sum(cases[k:k+j]) == missingNumber):
                return cases[k:k+j]
    return -1

missingNumber = 0
for i in range(25, len(cases)):
    if(not checkValid(i, 25)):
        missingNumber = cases[i]
        break

answerSet = findNumberSet(missingNumber)
# print(min(answerSet), max(answerSet)
print(min(answerSet) + max(answerSet))