
from collections import defaultdict

r = open("day8.txt", "r")
# r = open("test8.txt", "r")
# r = open("example8.txt", "r")
grid = list(map(list, r.read().splitlines()))
[print("".join(line)) for line in grid]

coords = defaultdict(list)
for j, row in enumerate(grid):
    for i, pos in enumerate(row):
        if pos != '.':
            coords[pos].append([i, j])

def getAllPairs(myList):
    res = []
    for i in range(len(myList)):
        for second in myList[i + 1:]:  
            res.append((myList[i], second))
    return res


# antinodes = set()
# for antenna in coords:
#     # print(antenna)
#     pairs = getAllPairs(coords[antenna])
#     # print(pairs)
#     for pair in pairs:
#         x1, y1 = pair[0]
#         x2, y2 = pair[1]
#         # print(x1, y1, x2, y2)
#         xDist = x2 - x1
#         yDist = y2 - y1
#         if xDist > 0:
#             newX1 = x1 - abs(xDist)
#             newX2 = x2 + abs(xDist)
#         else:
#             newX1 = x1 + abs(xDist)
#             newX2 = x2 - abs(xDist)
#         if yDist > 0:
#             newY1 = y1 - abs(yDist)
#             newY2 = y2 + abs(yDist)
#         else:
#             newY1 = y1 + abs(yDist)
#             newY2 = y2 - abs(yDist)
#         coord1 = (newX1, newY1)
#         coord2 = (newX2, newY2)
#         if 0 <= newX1 < len(grid[0]) and 0 <= newY1 < len(grid): #coord1 within bounds
#             if grid[newY1][newX1] == '.':
#                 grid[newY1][newX1] = '#'
#             antinodes.add(coord1)
#         if 0 <= newX2 < len(grid[0]) and 0 <= newY2 < len(grid): #coord1 within bounds
#             if grid[newY2][newX2] == '.':
#                 grid[newY2][newX2] = '#'
#             antinodes.add(coord2)
# # print(antinodes)
# print("part 1: ", len(antinodes))

antinodes = set()
for antenna in coords:
    # print(antenna)
    pairs = getAllPairs(coords[antenna])
    # print(pairs)
    for pair in pairs:
        x1, y1 = pair[0]
        x2, y2 = pair[1]
        antinodes.add((x1, y1))
        antinodes.add((x2, y2))
        xDist = x2 - x1
        yDist = y2 - y1
        if (x1 == x2):
            yDist = 1 if yDist > 0 else -1
        if (y1 == y2):
            xDist = 1 if xDist > 0 else -1
        if x1 == x2 and y1 == y2:
            xDist = 1 if xDist > 0 else -1
            yDist = 1 if yDist > 0 else -1
        if xDist > 0:
            updateX1 = 0 - abs(xDist)
            updateX2 = abs(xDist)
        else:
            updateX1 = abs(xDist)
            updateX2 = 0 - abs(xDist)
        newX1 = x1 + updateX1
        newX2 = x2 + updateX2
        if yDist > 0:
            updateY1 = 0 - abs(yDist)
            updateY2 = abs(yDist)
        else:
            updateY1 = abs(yDist)
            updateY2 = 0 - abs(yDist)
        newY1 = y1 + updateY1
        newY2 = y2 + updateY2
        coord1 = (newX1, newY1)
        coord2 = (newX2, newY2)
        while 0 <= newX1 < len(grid[0]) and 0 <= newY1 < len(grid): #coord1 within bounds
            if grid[newY1][newX1] == '.':
                grid[newY1][newX1] = '#'
            antinodes.add(coord1)
            newX1 += updateX1
            newY1 += updateY1
            coord1 = (newX1, newY1)
        while 0 <= newX2 < len(grid[0]) and 0 <= newY2 < len(grid): #coord2 within bounds
            if grid[newY2][newX2] == '.':
                grid[newY2][newX2] = '#'
            antinodes.add(coord2)
            newX2 += updateX2
            newY2 += updateY2
            coord2 = (newX2, newY2)
print("part 2: ", len(antinodes))

[print("".join(line)) for line in grid]