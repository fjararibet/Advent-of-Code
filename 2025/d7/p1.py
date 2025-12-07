import sys

input = open(sys.argv[1]).read()
grid = {}
start = (0, 0)
for i, line in enumerate(input.splitlines()):
    for j, c in enumerate(line):
        grid[i, j] = c
        if c == 'S':
            start = i, j
visited = set()
q = [start]
split_count = 0
while q:
    curr = q.pop()
    if curr in visited:
        continue
    if curr not in grid:
        continue
    visited.add(curr)
    i, j = curr
    if grid[curr] == '^':
        q.insert(0, (i, j-1))
        q.insert(0, (i, j+1))
        split_count += 1
    else:
        q.insert(0, (i+1, j))
print(split_count)
