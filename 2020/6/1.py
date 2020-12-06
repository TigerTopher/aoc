with open('input') as f:
    answers = "".join(f.readlines()).split("\n\n")

for i in range(0, len(answers)):
    answers[i] = answers[i].split("\n")

print(answers)

summer = 0
for answer in answers:
    setter = set("".join(answer))
    summer += len(setter)

print(summer)
