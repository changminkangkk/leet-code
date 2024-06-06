class Solution:
    def minimumChairs(self, s: str) -> int:
        currentOccupancy = 0
        maxOccupancy = 0

        for event in s:
            if event == 'E':
                currentOccupancy += 1
            else:
                currentOccupancy -= 1
            if currentOccupancy > maxOccupancy:
                maxOccupancy = currentOccupancy

        return maxOccupancy