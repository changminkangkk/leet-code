class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        # brute force approach O(N^2) runtime complexity
        # count = 0
        # for i in range(len(batteryPercentages)):
        #     if batteryPercentages[i] > 0:
        #         count += 1
        #         for j in range(i+1, len(batteryPercentages)):
        #             batteryPercentages[j] -= 1
        #             batteryPercentages[j] = max(0, batteryPercentages[j])
        # return count


        # Aim for O(N) solution:
       
        curr = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - curr > 0:
                curr += 1
        return curr