import math

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

memory = {}

mask = ""
bitMask = ""
zeroPositions = []
for op in cases:
    if(len(op.split("mask = ")) == 2):
        mask = op.split("mask = ")[1]
        zeroPositions = [(len(mask) - i - 1) for i, val in enumerate(mask) if val == '0']
        bitMask = mask.replace('X', '0')
    else:
        temp = op.split(" = ")
        memoryPosition = int(temp[0][4:-1])
        memoryValue = int(temp[1])

        maskedOutput = (memoryValue | int(bitMask, 2))
        for i in zeroPositions:
            maskedOutput = maskedOutput & ~(1 << i) # Erase bits in ith position
        memory[memoryPosition] = maskedOutput

print(sum(memory.values()))