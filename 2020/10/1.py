with open('input') as f:
    cases = [int(line.rstrip()) for line in f.readlines()]

builtIn = max(cases) + 3
cases = sorted(cases) + [builtIn]

joltDiff1 = 0
joltDiff3 = 0

print(cases)

lastNumber = 0
for i in range(0, len(cases)):
    print(cases[i], lastNumber)
    if(cases[i] - lastNumber == 1):
        joltDiff1 += 1
    if(cases[i] - lastNumber == 3):
        joltDiff3 += 1
    lastNumber = cases[i]
print(joltDiff1, joltDiff3, joltDiff1*joltDiff3)
