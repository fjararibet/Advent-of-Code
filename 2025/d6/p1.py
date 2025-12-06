import sys
from functools import reduce

input = open(sys.argv[1]).read().rstrip()
lines = input.splitlines()
ops = lines[-1].split()
numbers = [[int(n) for n in x.split()] for x in lines[:-1]]

result = 0
for j in range(len(ops)):
    op_numbers = []
    for i in range(len(numbers)):
        op_numbers.append(numbers[i][j])
    if ops[j] == "*":
        result += reduce(lambda x, y: x * y, op_numbers)
    else:
        result += sum(op_numbers)
print(result)
