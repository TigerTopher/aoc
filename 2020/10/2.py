with open('input') as f:
    cases = [int(line.rstrip()) for line in f.readlines()]

builtIn = max(cases) + 3
cases = [0] + sorted(cases) + [builtIn]

combinations = {
    0: 1
}
for i in range(1, len(cases)):
    sums = 0
    if(cases[i] - 3 >= 0 and cases[i]-3 in combinations):
        sums += combinations[cases[i] - 3]
    if(cases[i] - 2 >= 0 and cases[i]-2 in combinations):
        sums += combinations[cases[i] - 2]
    if(cases[i] - 1 >= 0 and cases[i]-1 in combinations):
        sums += combinations[cases[i] - 1]
    combinations[cases[i]] = sums

# print(combinations)
print(combinations[builtIn])
