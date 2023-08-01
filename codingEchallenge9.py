import re

def isSubsequence(s: str, t: str):
    s = [i for i in s]
    n = len(s)
    l = []
    for c in range(1, n):
        idx = re.search(s[c - 1], t)
        print('idx: ', idx.start())
        ix = re.search(s[c], t)
        if not idx.start() < ix.start():
            l.append(1)
    if len(l)>0:
        return False
    return True

s = "axc"
t = "ahbgdc"

print(isSubsequence(s,t))


