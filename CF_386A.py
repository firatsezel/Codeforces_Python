__author__ = 'forevercode'
#accepted

n = raw_input()
n = int(n)

Seq = [int(temp) for temp in raw_input().split(" ")]

current = Seq[0]
currentcount = 0

for Temp in range(len(Seq)):
    sTemp = Seq[Temp]
    if sTemp > current:
        current = sTemp
        currentcount = Temp

currentcount += 1
Seq.sort()
price = Seq[-2]

print currentcount, price