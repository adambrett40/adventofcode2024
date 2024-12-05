from collections import defaultdict

r = open('day5.txt', 'r')
# r = open('example5.txt', 'r')
content = r.read()
rules, updates = content.split('\n\n')
rules = rules.splitlines()
prereqs = defaultdict(list) #{number: [prereqs]}
for rule in rules:
    prereq, num = rule.split('|')
    prereqs[num].append(prereq)
# print(prereqs)
updates = list(map(lambda s: s.split(','), updates.splitlines()))
# print(updates)
def isPageValid(prereqs, pageSet, seen, page):
    for req in prereqs[page]:
        if req in pageSet and req not in seen:
            return False
    return True

def isUpdateValid(prereqs, update):
    pageSet = set(update)
    seen = set()
    for page in update:
        if not isPageValid(prereqs, pageSet, seen, page):
            return False
        seen.add(page)
    return True

def fixOrdering(update):
    pageSet = set(update)
    seen = set()
    for i in range(len(update)):
        if not isPageValid(prereqs, pageSet, seen, update[i]):
            for j in range(i, len(update)):
                if isPageValid(prereqs, pageSet, seen, update[j]):
                    page = update.pop(j)
                    update.insert(i, page)
                    break
        seen.add(update[i])
    return update

total = 0
# print('prereqs: ', prereqs)
for update in updates:
    validUpdate = isUpdateValid(prereqs, update)
    if not validUpdate:
        update = fixOrdering(update)
        total += int(update[len(update) // 2])
print(total)
    