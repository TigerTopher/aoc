with open('input') as f:
    testCase = [line.rstrip() for line in f.readlines()]

validCount = 0

for case in testCase:
    splits = case.split(": ")
    letter = splits[0].split(" ")[1]
    rangeMin = int(splits[0].split(" ")[0].split("-")[0])
    rangeMax = int(splits[0].split(" ")[0].split("-")[1])
    password = splits[1]

    condition = password.count(letter) >= rangeMin and password.count(letter) <= rangeMax
    if(condition):
        validCount += 1

    # print(letter, rangeMin, rangeMax, password, "is valid: ", condition)

print(validCount)
