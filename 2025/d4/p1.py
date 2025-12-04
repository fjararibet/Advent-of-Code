import sys

input = open(sys.argv[1]).read().rstrip()
grid = input.splitlines()

result = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            continue
        count = 0
        for n in range(i-1, i+2):
            for m in range(j-1, j+2):
                if n == i and m == j:
                    continue
                if n < 0 or n >= len(grid):
                    continue
                if m < 0 or m >= len(grid[0]):
                    continue
                if grid[n][m] == "@":
                    count += 1
        if count < 4:
            result += 1
print(result)
