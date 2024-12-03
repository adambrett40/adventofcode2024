r = open('day2.txt', 'r')
# r = open('example2.txt', 'r')
content = r.read()
reports = content.splitlines()

def isSafe(num1, num2, increasing):
    diff = num1 - num2
    if increasing:
        if (diff > -1 or diff < -3):
            return False
    else:
        if (diff < 1 or diff > 3):
            return False
    return True

def isReportSafe(report): 
    if (len(report) < 2): #safe automatically
        return True
    increasing = (report[0] < report[1])
    i = 0
    while (i < len(report) - 1):
        if (not isSafe(report[i], report[i+1], increasing)):
            return False
        i += 1
    return True

def partOne(reports):
    numsafe = 0
    for report in reports:
        levels = list(map(int, (report.split(" "))))
        if (isReportSafe(levels)): 
            numsafe += 1
    print("safe part 1: ", numsafe)

#O(n * m^2) where n = len(reports), m = len(report)
#should be able to make it O(n * m)
def partTwo(reports):
    numsafe = 0
    for report in reports:
        levels = list(map(int, (report.split(" "))))
        if (not isReportSafe(levels)): #unsafe
            for i in range(len(levels)): #go through whole report
                lvlcopy = levels.copy()
                lvlcopy.pop(i) #try removing each level individually
                if (isReportSafe(lvlcopy)): #if removing a single one works
                    numsafe += 1
                    break
        else: #safe
            numsafe += 1
    print("safe part 2: ", numsafe)

partOne(reports)
partTwo(reports)