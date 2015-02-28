__author__ = 'forevercode'
#wrong answer on test 4

n, m, k = [int(temp) for temp in raw_input().split(" ")]
result = []
Temparray = []
array = []
counter = 0

if k == 0:
    for a in range(n):
        myList = [int(count) for count in raw_input().split(" ")]
        TempList = [int(kadet) for kadet in myList]
        TempList.sort()
        if len(result) == 0:
            for i in range(len(myList) - 1):
                sTemp = myList[i]
                if sTemp > TempList[i]:
                    current = i
                    find = TempList[i]
                    current += 1
                    while myList[current] != find:
                        current += 1
                    eTemp = myList[current]
                    myList[current] = sTemp
                    myList[i] = eTemp
                    resulti = str(i + 1)
                    resultc = str(current + 1)
                    resultf = resulti + "_" + resultc
                    result.append(resultf)
                    counter += 1
        else:
            while len(result) != 0:
                mTemp = result.pop()
                Temparray.append(mTemp)
                array = [str(deneme) for deneme in mTemp.split("_")]
                index1 = array[0]
                index2 = array[1]
                index1 = int(index1) - 1
                index2 = int(index2) - 1
                if myList[index1] > myList[index2]:
                    eTemp = myList[index2]
                    myList[index2] = myList[index1]
                    myList[index1] = eTemp
            while len(Temparray) != 0:
                result.append(Temparray.pop())
            if myList != TempList:
                for i in range(len(myList) - 1):
                    sTemp = myList[i]
                    if sTemp > TempList[i]:
                        current = i
                        find = TempList[i]
                        current += 1
                        while myList[current] != find:
                            current += 1
                        eTemp = myList[current]
                        myList[current] = sTemp
                        myList[i] = eTemp
                        resulti = str(i + 1)
                        resultc = str(current + 1)
                        resultf = resulti + "_" + resultc
                        result.append(resultf)
                        counter += 1
else:
    for a in range(n):
        myList = [int(count) for count in raw_input().split(" ")]
        TempList = [int(kadet) for kadet in myList]
        TempList.sort(reverse=True)
        if len(result) == 0:
            for i in range(len(myList) - 1):
                sTemp = myList[i]
                if sTemp < TempList[-i]:
                    current = i
                    find = TempList[-i]
                    current += 1
                    while myList[current] != find:
                        current += 1
                    eTemp = myList[current]
                    myList[current] = sTemp
                    myList[i] = eTemp
                    resulti = str(i + 1)
                    resultc = str(current + 1)
                    resultf = resultc + "_" + resulti
                    result.append(resultf)
                    counter += 1
        else:
            while len(result) != 0:
                mTemp = result.pop()
                Temparray.append(mTemp)
                array = [str(deneme) for deneme in mTemp.split("_")]
                index1 = array[0]
                index2 = array[1]
                index1 = int(index1) - 1
                index2 = int(index2) - 1
                if myList[index1] > myList[index2]:
                    eTemp = myList[index2]
                    myList[index2] = myList[index1]
                    myList[index1] = eTemp
            while len(Temparray) != 0:
                result.append(Temparray.pop())
            if myList != TempList:
                for i in range(len(myList) - 1):
                    sTemp = myList[i]
                    if sTemp < TempList[-i]:
                        current = i
                        find = TempList[-i]
                        current += 1
                        while myList[current] != find:
                            current += 1
                        eTemp = myList[current]
                        myList[current] = sTemp
                        myList[i] = eTemp
                        resulti = str(i + 1)
                        resultc = str(current + 1)
                        resultf = resultc + "_" + resulti
                        result.append(resultf)
                        counter += 1


print counter
while len(result) != 0:
    mTemp = result.pop()
    array = [str(deneme) for deneme in mTemp.split("_")]
    print array[0], array[1]