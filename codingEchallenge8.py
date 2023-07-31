import re

def isPalindrome(s: str):
    b = ''
    for i in s.lower():
        if i.isalnum():
            b = b + i
    return b == b[::-1]
        


print(isPalindrome("0P"))


