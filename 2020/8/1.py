with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

accumulator = 0
index = 0
tagged = [0]*len(cases)

while True:
    if(tagged[index] == 1):
        break

    action = cases[index].split(" ")
    tagged[index] = 1

    if(action[0] == "acc"):
        accumulator += int(action[1])
        index += 1

    if(action[0] == "nop"):
        index = index + 1
    
    if(action[0] == "jmp"):
        index = index + int(action[1])

print(accumulator)