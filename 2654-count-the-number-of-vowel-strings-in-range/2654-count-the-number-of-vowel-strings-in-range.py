class Solution:
    def isVowel(self, char):
        return True if char in ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u') else False
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            wordLen = len(words[i])
            if self.isVowel(words[i][0]) and self.isVowel(words[i][-1]):
                count += 1 
        return count