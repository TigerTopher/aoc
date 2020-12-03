with open('input') as f:
    numList = [int(line.rstrip()) for line in f.readlines()]

for i in range(0, len(numList)):
    for j in range(i + 1, len(numList)):
        if(numList[i] + numList[j] == 2020):
            print(numList[i], numList[j], numList[i]*numList[j])