with open('input') as f:
    testCase = [line.rstrip() for line in f.readlines()]

validCount = 0

for case in testCase:
    splits = case.split(": ")
    letter = splits[0].split(" ")[1]
    position1 = int(splits[0].split(" ")[0].split("-")[0])
    position2 = int(splits[0].split(" ")[0].split("-")[1])
    password = splits[1]

    condition = (password[position1 - 1] == letter or password[position2 - 1] == letter) and password[position1 - 1] != password[position2 - 1]
    if(condition):
        validCount += 1

    print(letter, position1, position2, password, "is valid: ", condition)

print(validCount)
