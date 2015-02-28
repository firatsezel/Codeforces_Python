__author__ = 'forevercode'
#accepted

n, m = [int(temp) for temp in raw_input().split(" ")]
myList = [int(temp) for temp in raw_input().split(" ")]

myList.sort()
flag = None
i = 0
Cup = 0

while flag is None and i < n - 1:
    sTemp = myList[i]
    Cup += sTemp
    if Cup > m:
        flag = False
        break
    else:
        i += 1

if flag is None:
    print "YES"
elif flag is False:
    print "NO"