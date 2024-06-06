class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <3:
            return -1
        else:
            max1 = max(nums)
            min1 = min(nums)
            nums.remove(max1)
            nums.remove(min1)
            return nums[0]