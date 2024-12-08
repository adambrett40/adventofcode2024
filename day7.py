r = open("day7.txt", 'r')
# r = open("example7.txt", 'r')
content = r.read()
lines = content.splitlines()

print(lines)

def checkCalibration(target, nums): 
    # if acc > target:
    #     return False
    # if len(nums) == 0:
    #     return acc == target
    if len(nums) == 1:
        return nums[0] == target #or acc * nums[0] == target
    else:
        next = nums.pop(1)
        addnums = nums.copy()
        multnums = nums.copy()
        concnums = nums.copy()
        addnums[0] += next
        multnums[0] *= next
        concnums[0] = int(str(concnums[0]) + str(next))
        # if checkCalibration(target, acc + next, nums):
        #     return True
        # if checkCalibration(target, acc * next, nums):
        #     return True
        # return False
        return checkCalibration(target, addnums) or checkCalibration(target, multnums) or checkCalibration(target, concnums)


total = 0
for line in lines:
    spl = line.split(": ")
    target = int(spl[0])
    nums = list(map(int, spl[1].split(" ")))
    print(target)
    print(nums)
    if checkCalibration(target, nums):
        print("adding ", target)
        total += target
print(total)