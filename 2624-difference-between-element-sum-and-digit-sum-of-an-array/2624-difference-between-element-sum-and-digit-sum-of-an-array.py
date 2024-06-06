class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        a=sum(nums)
        b=0

        for i in nums:
            for j in str(i):
                b=b+int(j)
        
        return a-b


        