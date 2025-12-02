import sys

input = open(sys.argv[1]).read().rstrip()
lines = input.split("\n")
clock = 50
result = 0
for line in lines:
    if line.startswith("R"):
        clock = (clock + int(line[1:])) % 100
    else:
        clock = (clock - int(line[1:])) % 100
    if clock == 0:
        result += 1
print(result)



