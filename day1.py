from collections import defaultdict


l = open('day1.txt', 'r')
content = l.read()
content = content.splitlines()
print (len(content))
list1, list2 = [], []
for pair in content:
    # print(pair)
    spl = pair.split("   ")
    list1.append(int(spl[0])) 
    list2.append(int(spl[1])) 
# print(len(list1))
list1.sort()
list2.sort()


#q1:
# print(list1[0:10])
# dist = 0
# for i in range(len(list1)):
#     dist += abs(list1[i] - list2[i])
# print(dist)

#q2
# nums = {}
# for n in list2:
#     nums[n] = nums.get(n, 0) + 1
# print(nums)
# set1 = set(list1)
# similarity = 0
# for i, n in enumerate(list1):
#     if i > 0 and list1[i-1] == n:
#         continue
#     similarity += n * nums.get(n, 0)
# print (similarity)

#q2 without hashmap:
r = 0
similarity = 0
for i, n in enumerate(list1):
    if (list2[r] > n):
        continue
    if (i > 0 and list1[i-1] != n):
        while list2[r] < n:
            r += 1
        count = 0
        while list2[r] == n:
            count += 1
            r += 1
        similarity += count * n
print(similarity)