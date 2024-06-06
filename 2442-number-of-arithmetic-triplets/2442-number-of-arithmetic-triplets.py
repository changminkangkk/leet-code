class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if self.contains(nums, nums[i] + diff) and self.contains(nums, nums[i] + 2 * diff):
                counter += 1
        return counter

    def contains(self, nums: List[int], target: int) -> bool:
        return target in nums