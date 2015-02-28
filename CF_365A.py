__author__ = 'forevercode'
#time limit error on test 11

n, m = [int(temp) for temp in raw_input().split(" ")]

my = [0 for a in range(n)]
print 5
strs = ""
oldwinner = 0
for count in range(m):
    myList = [int(sayac) for sayac in raw_input().split(" ")]
    range1 = myList[0]
    range2 = myList[1]
    gamewinner = myList[2]
    if gamewinner == oldwinner and oldrange1 - 1 == range1:
        rTemp = range1 - 1
        if my[rTemp] == 0:
            my[rTemp] = gamewinner
    else:
        for g in range(range1, range2 + 1):
            counter = g - 1
            if my[counter] == 0 and counter != gamewinner - 1:
                my[counter] = gamewinner
    oldwinner = gamewinner
    oldrange1 = range1
    if count == m - 1:
        tourwinner = gamewinner
        my[tourwinner - 1] = 0

for step in range(len(my)):
    strs += str(my[step]) + " "
print strs


