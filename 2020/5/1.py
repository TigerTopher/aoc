import math

with open('input') as f:
    boarding_passes = [line.rstrip() for line in f.readlines()]

def findRow(pattern):
    start = 0
    end = 127
    # F - lower half
    # B - upper half
    for char in pattern:
        if char == 'F':
            end = (start + end) // 2
        if char == 'B':
            start = math.ceil((start + end)/ 2)
    return start

def findColumn(pattern):
    start = 0
    end = 7
    # F - lower half
    # B - upper half

    for char in pattern:
        print(char, '-', start, end)
        if char == 'L':
            end = (start + end) // 2
        if char == 'R':
            start = math.ceil((start + end)/ 2)
    return start

print(findRow('FFFFFFF'))
print(findRow('FFFFFFB'))
print(findRow('BBBBBBB'))

## F -> 0
## B -> 1

print(findRow('FBFBBFF'))
print(findRow('BBBBBBB'))
print(findColumn('RLR'))

seat_ids = []
rows_columns = []

max_value = -1
max_row = -1
max_column = -1

for boarding_pass in boarding_passes:
    row = findRow(boarding_pass[:7])
    column = findColumn(boarding_pass[-3:])
    idVal = (row*8) + column
    seat_ids.append(idVal)
    rows_columns.append([row, column])
    print(boarding_pass)
    if(idVal > max_value):
        max_value = idVal
        max_row = row
        max_column = column

print(seat_ids)
print(max(seat_ids))
print(max_row, max_column, max_value)
print(len(boarding_passes))
print(sorted(seat_ids))

seats = sorted(seat_ids)
for i in range(0, len(seats)-1):
    if(not seats[i]+1 == seats[i+1]):
        print(seats[i], seats[i+1])

print(seats)