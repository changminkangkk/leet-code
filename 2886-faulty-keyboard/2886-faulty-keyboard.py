class Solution:
    def finalString(self, s: str) -> str:
        result = []
        reverse = False
        for char in s:
            if char == 'i':
                reverse = not reverse
            else:
                if reverse:
                    result.insert(0, char)
                else:
                    result.append(char)
        if reverse:
            result.reverse()
        return ''.join(result)