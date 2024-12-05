# r = open('day4.txt', 'r')
r = open('example4.txt', 'r')
content = r.read()
lines = content.splitlines()
# validWords = 0
# for y, line in enumerate(lines):
#     for x, letter in enumerate(line):
#         if letter == 'X':
#             right = len(line) > x+3 
#             left = x >= 3
#             up = y >= 3
#             down = len(lines) > y+3
#             if right and line[x+1] == 'M' and line[x+2] == 'A' and line[x+3] == 'S': #right
#                 validWords += 1
#             if left and line[x-1] == 'M' and line[x-2] == 'A' and line[x-3] == 'S': #left
#                 validWords += 1
#             if up and lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S': #up
#                 validWords += 1
#             if down and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S': #down
#                 validWords += 1
#             if up and right and lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S': #up and right
#                 validWords += 1
#             if down and right and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S': #down and right
#                 validWords += 1
#             if up and left and lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S': #up and left
#                 validWords += 1
#             if down and left and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S': #down and left
#                 validWords += 1
# print("part 1", validWords)

validWords = 0
for y, line in enumerate(lines):
    for x, letter in enumerate(line):
        if letter == 'A':
            right = len(line) > x+1
            left = x >= 1
            up = y >= 1
            down = len(lines) > y+1
            if left and right and up and down:
                tlm = lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S'
                tls = lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M'
                trm = lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S'
                trs = lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M'
                if (tlm or tls) and (trm or trs):
                    validWords += 1
print("part 2", validWords)