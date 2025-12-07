import sys


def myfind(arr, pos):
    for i, (p, weight) in enumerate(arr):
        if p == pos:
            return i
    return None


input = open(sys.argv[1]).read()
grid = {}
start = (0, 0)
for i, line in enumerate(input.splitlines()):
    for j, c in enumerate(line):
        grid[i, j] = c
        if c == 'S':
            start = i, j
visited = set()
q = [(start, 1)]
timeline_count = 1

while q:
    curr, weight = q.pop()
    if curr in visited:
        continue
    if curr not in grid:
        continue
    visited.add(curr)
    i, j = curr
    if grid[curr] == '^':
        for y in [j-1, j+1]:
            n = myfind(q, (i, y))
            if n is not None:
                p, w = q[n]
                q[n] = (p, w + weight)
            else:
                q.insert(0, ((i, y), weight))

        timeline_count += weight
    else:
        q.insert(0, ((i+1, j), weight))
print(timeline_count)
