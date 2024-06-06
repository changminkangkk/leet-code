class Solution:
    def numberOfSteps(self, n: int) -> int:
        step=0
        while n!=0:
            if n%2==0:
                n/=2
                step+=1
            else:
                n-=1
                step+=1
        return step