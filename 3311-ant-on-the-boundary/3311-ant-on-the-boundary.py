class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # Variable to store the Num. of Steps which we are far from the Boundary
        steps_far_from_bound = 0 # SC : O(1)
        ans = 0 # Answer
        for i in range(len(nums)): # TC : O(n)
            steps_far_from_bound += nums[i] # Updating Boundary Steps
            # If Number of Boundary Steps(After Updating) gets equals to 0,, then we cam back to Boundary Again
            if steps_far_from_bound == 0: 
                ans += 1
        return ans