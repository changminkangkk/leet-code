class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                answer += num ** 2

        return answer

        