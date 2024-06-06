class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        nums=sorted(nums)
        for i in range(0,len(nums),2):
            res.extend(nums[i:i+2][::-1])
        return res