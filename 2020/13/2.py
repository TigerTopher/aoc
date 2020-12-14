# Slow
import math
with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

personArrivalTime = int(cases[0])

busTimes = cases[1].split(",")

for i in range(0, len(busTimes)):
    if busTimes[i] != "x":
        busTimes[i] = int(busTimes[i])

currentTime = busTimes[0]
startTime = busTimes[0]

while True:
    startRange = currentTime
    endRange = currentTime + startTime

    diffs = [0]
    times = [startRange]

    for i in range(1, len(busTimes)):
        if(busTimes[i] == "x"):
            diffs.append('x')
            times.append((times[i-1] + 1))
        else:
            diffs.append((math.ceil(currentTime/busTimes[i])*busTimes[i]) - currentTime)
            times.append(math.ceil(currentTime/busTimes[i])*busTimes[i])

    ascending = True

    for i in range(0, len(times)):
        if (times[i] > endRange):
            ascending = False

    for i in range(0, len(times) -1):
        if(times[i] +1 != times[i+1]):
            ascending = False

    # print(startRange, times, ascending)
    if(ascending):
        print(diffs)
        print(startRange)
        print(times)
        exit()
    # Get bus times
    # Test if ascending
    # Everything is within startRange and endRange

    currentTime += startTime
# print(busTimes)

# minimumWaitingTime = 99999999
# fastestBusId = 9999999999

# for time in busTimes:
#     waitingTime = (math.ceil(personArrivalTime/time)*time) - personArrivalTime
#     if(waitingTime < minimumWaitingTime):
#         minimumWaitingTime = waitingTime
#         fastestBusId = time

# busId = fastestBusId
# print(minimumWaitingTime*fastestBusId)
# print((minimumWaitingTime*fastestBusId) - personArrivalTime)
# print(fastestBusId*minimumWaitingTime)
# print((minimumWaitingTime*fastestBusId) - personArrivalTime, '*', fastestBusId)
# print("Answer", ((minimumWaitingTime*fastestBusId) - personArrivalTime) *fastestBusId)
