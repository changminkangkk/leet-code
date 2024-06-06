class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        for i in range(len(words)):
            words[i] = words[i].split(separator)
        
        ans = []
        for word in words:
            ans += word
        
        a = []
        for word in ans:
            if word != '':
                a.append(word)

        return a