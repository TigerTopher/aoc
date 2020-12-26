with open('input') as f:
    cases = f.readlines()[0]

initial_number = list(map(lambda x: int(x), cases[1:-1].split(',')))

lastSpoken = {}
turnArray = initial_number[:]

for i in range(0, len(initial_number)):
    lastSpoken[initial_number[i]] = [i+1]

turnNumber = len(initial_number)
lastNumber = initial_number[-1]

while (turnNumber < 30000000):
    if (lastNumber in lastSpoken and len(lastSpoken[lastNumber]) > 1):
        lastSpokenArray = lastSpoken[lastNumber]
        diffValue = lastSpokenArray[-1] - lastSpokenArray[-2]
        lastNumber = diffValue
    else:
        lastNumber = 0

    if lastNumber in lastSpoken:
        lastSpoken[lastNumber] = lastSpoken[lastNumber][-1:] + [turnNumber + 1]
    else:
        lastSpoken[lastNumber] = [turnNumber + 1]

    turnNumber += 1

print(lastNumber)
