from collections import defaultdict
import copy


r = open('day6.txt', 'r')
# r = open('example6.txt', 'r')
content = r.read()
rows = content.splitlines()
found = False
for y, row in enumerate(rows):
    rows[y] = list(row)
    for x, val in enumerate(row):
        if val == '^':
            print("found", x, y)
            pos = [x, y]
            break
# print(rows)
def next(dir):
    if dir == (0, -1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, 1)
    elif dir == (0, 1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, -1)
    else:
        return -1
    
def hasLoop(rows, x, y, dir):
    seen = defaultdict(set)
    while y >= 0 and y < len(rows) - 1 and x >= 0 and x < len(rows[y]) - 1: #while still in bounds
        if rows[y + dir[1]][x + dir[0]] == '#':
            dir = next(dir)
        if (x + dir[0],y + dir[1]) in seen and dir in seen[(x + dir[0],y + dir[1])]:
            return True
        
        seen[(x, y)].add(dir)
        x = x + dir[0]
        y = y + dir[1]
    return False

x, y = pos
seen = defaultdict(set)
dir = (0, -1) #[x, y] [0, -1] -> [1, 0] -> [0, 1] -> [-1, 0] -> [0, -1]
total = 0
while y >= 0 and y < len(rows) - 1 and x >= 0 and x < len(rows[y]) - 1: #while still in bounds
    if rows[y + dir[1]][x + dir[0]] == '#':
        dir = next(dir)
    seen[(x, y)].add(dir)
    # rows[y][x] = 'X'
    x = x + dir[0]
    y = y + dir[1]
seen[(x, y)].add(dir)
seen.pop((pos[0], pos[1]))
for coord in seen:
    prev = rows[coord[1]][coord[0]]
    rows[coord[1]][coord[0]] = '#'
    if hasLoop(rows, pos[0], pos[1], (0, -1)):
        total += 1
    rows[coord[1]][coord[0]] = prev
print("part 1", len(seen))
#4 too many???? why????
print("part 2", total)