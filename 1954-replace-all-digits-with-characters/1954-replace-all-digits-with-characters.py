class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c, x):
            return chr(ord(c) + x)
        result = []
        t = list(s)
        for i in range(len(t)):
            if t[i].isdigit():
                result.append(shift(t[i-1], int(t[i])))
            else:
                result.append(t[i])
                
        return "".join(result)