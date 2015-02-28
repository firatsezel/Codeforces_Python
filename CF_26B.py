__author__ = 'forevercode'
#accepted

mySequence = raw_input()
mySequence = str(mySequence)

Seq1 = [str("") for temp in range(len(mySequence))]
Seq2 = [str("") for sTemp in range(len(mySequence))]
Stack1 = []
Stack2 = []

i = 0
i1 = 0
i2 = 0
useless = 0
bool = None

while i < len(mySequence):
    Temp = mySequence[i]
    if Temp == ")" and bool is None:
        useless += 1
    elif Temp == "(":
        bool = True
        Stack1.append(Temp)
    else:
        Stack2.append(Temp)
        if len(Stack1) != 0:
            mTemp = Stack1.pop()
            if mTemp == "(":
                Stack2.pop()
            else:
                bool = None

    i += 1

result = useless + len(Stack2) + len(Stack1)

finalresult = len(mySequence) - result

print finalresult