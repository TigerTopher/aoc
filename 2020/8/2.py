with open('input') as f:
    actualCases = [line.rstrip() for line in f.readlines()]

def executeCode(cases):
    accumulator = 0
    index = 0
    tagged = [0]*len(cases)

    try:
        while True:
            if(index == len(tagged)):
                print(accumulator)
                return accumulator

            if(tagged[index] == 1):
                break

            action = cases[index].split(" ")
            tagged[index] = 1

            if(action[0] == "acc"):
                accumulator += int(action[1])
                index += 1

            elif(action[0] == "nop"):
                index = index + 1

            elif(action[0] == "jmp"):
                index = index + int(action[1])
    except:
        pass

for i in range(0, len(actualCases)):
    if(actualCases[i].split(" ")[0] == "jmp"):
        copyCase = actualCases.copy()
        copyCase[i] = "nop" + copyCase[i][3:]
        executeCode(copyCase)
    elif(actualCases[i].split(" ")[0] == "nop"):
        copyCase = actualCases.copy()
        copyCase[i] = "jmp" + copyCase[i][3:]
        executeCode(copyCase)
