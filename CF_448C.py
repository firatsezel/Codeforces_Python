__author__ = 'forevercode'
#wrong answer test 9 (aşgorithm failed)

n = raw_input()
n = int(n)

myList = [int(temp) for temp in raw_input().split(" ")]
i = 0
fark = []
current = myList[0]
i += 1
action = 1
largest = current
fark.append(0)

while i < len(myList):
    sTemp = myList[i]
    if sTemp > current:
        largest = sTemp
    farktemp = current - sTemp
    if farktemp != 0:
        if farktemp not in fark:
            fark.append(farktemp)
            action += 1
    i += 1

if len(myList) > 1 and current == largest and current <= len(myList):
    count = current - 1
    action += count

print action