class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for x in hours:
            if x >= target:
                cnt += 1
        return cnt