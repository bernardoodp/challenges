import re

def isPalindrome(s: str):
    s = list(re.sub(r'[.,"\'-?:!;]', '', s))
    reverse = list(reversed(s))
    if ''.join(s).lower().replace(' ', '') == ''.join(reverse).lower().replace(' ', ''):
        return True
    return False



print(isPalindrome("race a car"))


