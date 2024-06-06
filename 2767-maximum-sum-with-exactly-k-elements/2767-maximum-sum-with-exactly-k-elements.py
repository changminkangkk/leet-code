class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        maxElement=nums[0]
        count=0
        for i in range(k):
            count+=maxElement
            maxElement+=1
        return count