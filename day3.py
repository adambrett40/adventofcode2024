import re
r = open('day3.txt', 'r')
# r = open('example3.txt', 'r')
# r = open('example3_2.txt', 'r')
content = r.read()
# parsed = re.findall(r'mul\(\d+,\d+\)', content) #/mul\(\d+,\d+\)/gm
# print(parsed)
# total = 0
# for mult in parsed:
#     a, b = map(int, re.findall(r'\d+', mult))
#     total += a * b
# print(total)




parsed = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', content) 
print(parsed)
total = 0
skip = False
for exp in parsed:
    if (exp == 'do()'):
        skip = False
        continue
    elif (exp == 'don\'t()'):
        skip = True
        continue
    if skip:
        continue
    a, b = map(int, re.findall(r'\d+', exp))
    total += a * b
print(total)