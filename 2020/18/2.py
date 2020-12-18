import re

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

# Operation wrapper
# Idea: You can overload python's operations (+, -, *, /) when dealing with Objects.
# Problem: Addition operation should precede multiplication
# Solution: Transform Multiplication to Addition, transform addition to multiplication
class Op(int):
    def __add__(self, second):
        return Op(int(self) * second)
    def __mul__(self, second):
        return Op(int(self) + second)

total_sum = 0
for operation in cases:
    operation = re.sub(r"(\d+)", r"Op(\1)", operation).replace("*", "$").replace("+", "*").replace("$", "+")
    total_sum += eval(operation, {}, {"Op": Op})

print(total_sum)
