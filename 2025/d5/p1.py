import sys

input = open(sys.argv[1]).read().rstrip()
line_ranges, line_ids = input.split("\n\n")
ranges = [range(int(r.split("-")[0]), int(r.split("-")[1])+1) for r in line_ranges.splitlines()]
ids = [int(x) for x in line_ids.splitlines()]

result = 0
for id in ids:
    for r in ranges:
        if id in r:
            result += 1
            break
print(result)
