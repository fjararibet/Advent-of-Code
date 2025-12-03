import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")

result = 0
for bank in lines:
    numbers = []
    curr_pos = 0
    for cut_length in reversed(range(12)):
        curr_max = 0
        for i in range(curr_pos, len(bank) - cut_length):
            if curr_max < int(bank[i]):
                curr_max = int(bank[i])
                curr_pos = i + 1
        numbers.append(str(curr_max))
    result += int(''.join(numbers))

print(result)
