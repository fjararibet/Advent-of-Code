import sys
import heapq
from functools import reduce

input = open(sys.argv[1]).read()

boxes = [tuple(int(x) for x in line.split(",")) for line in input.splitlines()]
distances = []
for i, b1 in enumerate(boxes):
    for b2 in boxes[i+1:]:
        if b1 == b2:
            continue
        i1, j1, k1 = b1
        i2, j2, k2 = b2
        d = (i1 - i2) ** 2 + (j1 - j2) ** 2 + (k1 - k2) ** 2
        heapq.heappush(distances, (d, b1, b2))
circuits = [{x} for x in boxes]

last = None
while len(circuits) > 1:
    d, b1, b2 = heapq.heappop(distances)
    last = b1, b2
    found = False
    idx1, idx2 = -1, -1
    for i, c in enumerate(circuits):
        if b1 in c:
            idx1 = i
            found = True
        if b2 in c:
            idx2 = i
            found = True
    if found:
        if idx1 == idx2:
            circuits[idx1].add(b1)
            circuits[idx1].add(b2)
        else:
            s = circuits[idx2]
            circuits[idx1] = circuits[idx1] | s
            circuits.pop(idx2)
    else:
        circuits.append({b1, b2})
circuits.sort(key=lambda x: -len(x))

print(last[0][0] * last[1][0])
