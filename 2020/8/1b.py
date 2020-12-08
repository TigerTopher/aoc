# No Ifs alternative but still with globals T_T

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

accumulator = 0
index = 0
tagged = [0]*len(cases)

def accumulate(value):
    global accumulator
    global index

    accumulator += int(action[1])
    index += 1

def nop(value):
    global accumulator
    global index

    index = index + 1

def jump(value):
    global accumulator
    global index

    index = index + int(action[1])

operations = {
    'acc': accumulate,
    'nop': nop,
    'jmp': jump,
}

def processOperation(action, value):
    tagged[index] = 1
    operations[action](value)

while True:
    if(tagged[index] == 1):
        break

    action = cases[index].split(" ")
    processOperation(*action)


print(accumulator)