# Option 2: Use set intersection of list
with open('input') as f:
    answers = "".join(f.readlines()).split("\n\n")

for i in range(0, len(answers)):
    answers[i] = answers[i].rstrip("\n").split("\n")

total_sum = 0

for answer in answers:
    for i in range(0, len(answer)):
        answer[i] = set(answer[i])

    total_sum += len(set.intersection(*answer))

print(total_sum)
