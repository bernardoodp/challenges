def lengthOfLastWord(s: str) -> int:
        s = s.rstrip()
        l = []
        for letter in s[::-1]:
                
                if letter == ' ':
                    break
                l.append(letter)
        ''.join(l)
        new = list(reversed(l))
        tamanho = len(l)
        return ''.join(new), tamanho
    
print(lengthOfLastWord("Hello World   "))




