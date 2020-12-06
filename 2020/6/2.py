with open('input') as f:
    answers = "".join(f.readlines()).split("\n\n")

for i in range(0, len(answers)):
    answers[i] = answers[i].rstrip("\n").split("\n")

total_sum = 0

for answer in answers:
    mini_sum = 0
    occur = len(answer)
    concated = "".join(answer)

    for char in "abcdefghijklmnopqrstuvwxyz":
        if(concated.count(char) == occur):
            mini_sum += 1
            print(answer, answer.count(char), occur, char)
    total_sum += mini_sum

print(total_sum)
