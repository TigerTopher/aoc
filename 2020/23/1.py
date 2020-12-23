cups = list("135468729")
# cups = list("389125467")
cups = [int(i) for i in cups]
min_value = min(cups)
max_value = max(cups)
pickup_count = 3
max_moves = 100

i = 0
moves = 1

while moves <= max_moves:
    current_cup = cups[i]
    pickup = cups[i+1:i+pickup_count+1]

    destination = cups[i] - 1
    while (destination in pickup or destination < min_value):
        if(destination in pickup):
            destination -= 1
        if(destination < min_value):
            destination = max_value

    print('-- move {move_number} --'.format(move_number=moves))
    print('cups: ({current_cup}) {other_cups}'.format(
        current_cup = current_cup,
        other_cups = cups[i+1:]
    ))
    print('pick up: {pickup}'.format(pickup=pickup))
    print('destination: {destination}'.format(destination=destination))

    destination_index = cups.index(destination)

    cups = cups[i+(pickup_count+1):destination_index+1] + pickup + cups[destination_index+1:] + [current_cup]
    print(cups)

    moves += 1
print(cups)