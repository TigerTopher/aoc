import math

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

memory = {}
mask = ""
floatingAddresses = []

def getFloatingAddresses(mask, i = 0):
    if(i >= len(mask)):
        floatingAddresses.append(int(mask, 2))
        return

    if(mask[i] == 'X'):
        tempMask = list(mask[:])
        tempMask[i] = '1'
        getFloatingAddresses(''.join(tempMask), i+1)
        tempMask[i] = '0'
        getFloatingAddresses(''.join(tempMask), i+1)
    else:
        getFloatingAddresses(mask, i+1)

def getBinaryAddress(memoryPosition, bit_length = 36):
    binaryAddress = str(bin(memoryPosition))[2:]
    return ('0' * (bit_length-len(binaryAddress)))+ str(bin(memoryPosition))[2:]

def bitMask(mask, binaryAddress):
    binaryAddress = list(binaryAddress)
    for i in range(len(mask)):
        if(mask[i] == 'X'):
            binaryAddress[i] = 'X'
        if(mask[i] == '1'):
            binaryAddress[i] = '1'
    return ''.join(binaryAddress)

for op in cases:
    if(len(op.split("mask = ")) == 2):
        mask = op.split("mask = ")[1]
    else:
        temp = op.split(" = ")
        memoryPosition = int(temp[0][4:-1])
        memoryValue = int(temp[1])

        binaryAddress = bitMask(mask, getBinaryAddress(memoryPosition))

        floatingAddresses = []
        getFloatingAddresses(binaryAddress)
        for floatingAddress in floatingAddresses:
            memory[floatingAddress] = memoryValue

print(sum(memory.values()))