import sys

input = open(sys.argv[1]).read().rstrip()
line_ranges, line_ids = input.split("\n\n")
ranges = [(int(r.split("-")[0]), int(r.split("-")[1])) for r in line_ranges.splitlines()]
ids = [int(x) for x in line_ids.splitlines()]

ranges = sorted(ranges)
while True:
    unique_ranges = []
    is_done = True
    for i in range(len(ranges)):
        a, b = ranges[i]
        is_unique = True
        for j in range(len(unique_ranges)):
            c, d = ranges[j]
            if max(a, c) <= min(b, d):
                unique_ranges[j] = (min(a, c), max(b, d))
                is_unique = False
                is_done = False
        if is_unique:
            unique_ranges.append((a, b))
    if is_done:
        break
    ranges = unique_ranges[:]


print(sum(b - a + 1 for a, b in unique_ranges))
