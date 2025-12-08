import sys
from functools import cache


def myfind(arr, pos):
    for i, (p, weight) in enumerate(arr):
        if p == pos:
            return i
    return None


def pp_grid(grid, n, m):
    for i in range(n):
        print(''.join(grid[i, j] for j in range(m)))
    print()


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
d_grid = grid.copy()
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
        d_grid[curr] = str(weight)
        q.insert(0, ((i+1, j), weight))


@cache
def solve(i, j):
    if (i, j) not in grid:
        return 1
    if grid[i, j] == '^':
        return solve(i, j-1) + solve(i, j+1)
    else:
        return solve(i+1, j)


print(timeline_count)
print(solve(start[0], start[1]))
