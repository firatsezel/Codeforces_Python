__author__ = 'forevercode'

n = raw_input()
n = int(n)

myList = [int(temp) for temp in raw_input().split(" ")]
sum = 0
Array = []
ResArray = []
TempArray = []
bool = None
total = 1000000
current = 0
cou = 1

for temp in range(len(myList)):
    sTemp = myList[temp]
    sum += sTemp - 1
    if sTemp not in Array:
        Array.append(sTemp)

if sum == 0:
    bool = False

if total > sum:
    fark = total - sum
    if total not in Array:
        ResArray.append(total)
    current = fark
    while bool is None:
        if current not in Array:
            ResArray.append(current)
            bool = True
        else:
            yukari = current + cou
            asagi = current - cou
            if yukari not in Array and asagi not in Array:
                ResArray.append(yukari)
                ResArray.append(asagi)
                bool = True
            elif yukari not in Array or asagi not in Array:
                while len(ResArray) != 0:
                    mTemp = ResArray.pop()
                    TempArray.append(mTemp)
                    if mTemp in Array:
                        current = mTemp
                        TempArray.pop()
                while len(TempArray) != 0:
                    mTemp = TempArray.pop()
                    ResArray.append(mTemp)
                cou = 1
            else:
                cou += 1
elif total < sum:
    fark = sum - total
    if 1 not in Array:
        ResArray.append(1)
        current = total - fark + 1
    else:
        for s in range(2, total):
            if s not in Array:
                ResArray.append(s)
                current = total - fark + s
    while bool is None:
        if current not in Array:
            ResArray.append(current)
            bool = True
        else:
            yukari = current + cou
            asagi = current - cou
            if yukari not in Array and asagi not in Array:
                ResArray.append(yukari)
                ResArray.append(asagi)
                bool = True
            elif yukari not in Array or asagi not in Array:
                while len(ResArray) != 0:
                    mTemp = ResArray.pop()
                    TempArray.append(mTemp)
                    if mTemp in Array:
                        current = mTemp
                        TempArray.pop()
                while len(TempArray) != 0:
                    mTemp = TempArray.pop()
                    ResArray.append(mTemp)
                cou = 1
            else:
                cou += 1
else:
    if total not in Array:
        bool = False
    else:
        cou = 1
        current = 500000
        while bool is None:
            if current not in Array:
                ResArray.append(current)
                bool = True
            else:
                yukari = current + cou
                asagi = current - cou
                if yukari not in Array and asagi not in Array:
                    ResArray.append(yukari)
                    ResArray.append(asagi)
                    bool = True
                elif yukari not in Array or asagi not in Array:
                    while len(ResArray) != 0:
                        mTemp = ResArray.pop()
                        TempArray.append(mTemp)
                        if mTemp in Array:
                            current = mTemp
                            TempArray.pop()
                    while len(TempArray) != 0:
                        mTemp = TempArray.pop()
                        ResArray.append(mTemp)
                    cou = 1
                else:
                    cou += 1

if bool is False:
    print 1
    print total
else:
    print len(ResArray)
    strLine = ""
    for d in range(len(ResArray)):
        strLine += str(ResArray.pop()) + " "
    print strLine