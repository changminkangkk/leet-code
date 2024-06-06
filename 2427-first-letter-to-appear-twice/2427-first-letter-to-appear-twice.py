class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visi = set()
        for i in s:
            if i in visi:
                return i
            else:
                visi.add(i)