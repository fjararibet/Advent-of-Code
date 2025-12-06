import sys
from functools import reduce

input = open(sys.argv[1]).read().rstrip()
lines = input.splitlines()
ops = lines[-1].split()
numbers = [x + " " for x in lines[:-1]]
curr_op = 0
op_nums = []
result = 0
for j in range(len(numbers[0])):
    curr_numbers = []
    for i in range(len(numbers)):
        if numbers[i][j].strip():
            curr_numbers.append(numbers[i][j])
    if not curr_numbers:
        if ops[curr_op] == "*":
            result += reduce(lambda x, y: x * y, op_nums)
        else:
            result += sum(op_nums)
        op_nums = []
        curr_op += 1
        continue
    op_nums.append(int(''.join(curr_numbers)))
