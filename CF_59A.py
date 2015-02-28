__author__ = 'forevercode'
#accepted

n = raw_input()
n = int(n)

AlcoholList = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
NumberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
Checking = 0

for Temp in range(n):
    Propan = raw_input()
    Propan = str(Propan)
    Propan = Propan.upper()
    if Propan in AlcoholList:
        Checking += 1
    else:
        if Propan[0] in NumberList:
            Age = int(Propan)
            if Age < 18:
                Checking += 1

print Checking