import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")

result = 0
for bank in lines:
    curr_max = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            curr_max = max(int(bank[i] + bank[j]), curr_max)
    result += curr_max
print(result)

