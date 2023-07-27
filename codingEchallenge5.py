def romanToInt(s: str) -> int:
        cList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        iList = []
        p = 1
        for key in cList:
            iList[key] = p
            if len(iList) % 2 == 0:
                p = p * 2
            else:
                p = p * 5
        print(iList)

cList = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
iList = []
p = 1
for key in cList:
    iList.append({key:p})
    if len(iList) % 2 == 0:
        p = p * 2
    else:
        p = p * 5
