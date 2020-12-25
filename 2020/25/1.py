with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

car_public_key = int(cases[0])
door_public_key = int(cases[1])

def find_loop_size(target_value):
    start_value = 1
    loop_size = 0
    while start_value != target_value:
        start_value *= 7
        start_value = start_value % 20201227
        loop_size += 1
    return loop_size

def perform_transformation(subject_number, loop_size):
    start_value = 1
    for i in range(0, loop_size):
        start_value *= subject_number
        start_value = start_value % 20201227
    return start_value

car_key_loop_size = find_loop_size(car_public_key)
door_key_loop_size = find_loop_size(door_public_key)

print(perform_transformation(door_public_key, car_key_loop_size))
print(perform_transformation(car_public_key, door_key_loop_size))
