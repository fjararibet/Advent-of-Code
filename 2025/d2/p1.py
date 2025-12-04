import sys

input = open(sys.argv[1]).read().rstrip()

id_ranges = input.split(",")
result = 0
for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]
    for id in range(start, end+1):
        id_str = str(id)
        if id_str[:len(id_str)//2] == id_str[len(id_str)//2:]:
            result += int(id)
print(result)
