import re

with open('input') as f:
    cases = [line.rstrip() for line in f.readlines()]

# Operation wrapper
# Idea: You can overload python's operations (+, -, *, /) when dealing with Objects.
# Problem: Operation is now left to right
# Solution: Transform Multiplication to Subtraction
# Since addition and subtraction have equal order of precedence, they will be executed as described
class Op(int):
    def __add__(self, b):
        return Op(int(self) + b)
    def __sub__(self, b):
        return Op(int(self) * b)

total_sum = 0
for operation in cases:
    operation = re.sub(r"(\d+)", r"Op(\1)", operation).replace("*", "-")
    total_sum += eval(operation, {}, {"Op": Op})

print(total_sum)
