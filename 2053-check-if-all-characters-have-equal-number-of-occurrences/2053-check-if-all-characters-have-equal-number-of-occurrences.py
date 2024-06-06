class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        hashMap = defaultdict(int)

        for i in s:
            hashMap[i] = hashMap[i] + 1

        # obtaining the first value in dictionary
        firstValue = next(iter(hashMap.values()))

        for i in hashMap.values():
            if i != firstValue:
                return False

        return True
        