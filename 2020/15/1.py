with open('input') as f:
    cases = f.readlines()[0]

initial_number = list(map(lambda x: int(x), cases[1:-1].split(',')))
lastSpoken = {}
turnArray = initial_number[:]

for i in range(0, len(initial_number)):
    lastSpoken[initial_number[i]] = [i+1]

turnNumber = len(initial_number)
while (len(turnArray) != 2020):
    if (turnArray[-1] in lastSpoken and len(lastSpoken[turnArray[-1]]) > 1):
        lastSpokenArray = lastSpoken[turnArray[-1]]
        diffValue = lastSpokenArray[-1] - lastSpokenArray[-2]
        turnArray.append(diffValue)
    else:
        turnArray.append(0)

    if turnArray[-1] in lastSpoken:
        lastSpoken[turnArray[-1]] += [turnNumber + 1]
    else:
        lastSpoken[turnArray[-1]] = [turnNumber + 1]

    turnNumber = len(turnArray)

print(turnArray[-1])
