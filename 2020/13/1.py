import math
with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

personArrivalTime = int(cases[0])


busTimes = [] 
unP = cases[1].split(",")
for i in range(0, len(unP)):
    if unP[i] != "x":
        busTimes.append(int(unP[i]))

print(busTimes)

minimumWaitingTime = 99999999
fastestBusId = 9999999999

for time in busTimes:
    waitingTime = (math.ceil(personArrivalTime/time)*time) - personArrivalTime
    if(waitingTime < minimumWaitingTime):
        minimumWaitingTime = waitingTime
        fastestBusId = time

busId = fastestBusId
print(minimumWaitingTime*fastestBusId)
# print((minimumWaitingTime*fastestBusId) - personArrivalTime)
# print(fastestBusId*minimumWaitingTime)
# print((minimumWaitingTime*fastestBusId) - personArrivalTime, '*', fastestBusId)
# print("Answer", ((minimumWaitingTime*fastestBusId) - personArrivalTime) *fastestBusId)
