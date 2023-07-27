def romanToInt(s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        rs = 0
        for rome in range(len(s)):
            if rome < len(s)-1 and roman[s[rome]] < roman[s[rome + 1]]:
                rs -= roman[s[rome]]
            else: 
                rs += roman[s[rome]]
        return rs