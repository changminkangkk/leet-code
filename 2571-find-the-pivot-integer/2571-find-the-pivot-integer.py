class Solution:
    def pivotInteger(self, n: int) -> int:
        li,c=[i for i in range(1,n+1)],-1
        for i in range(len(li)):
            if sum(li[0:i+1])==sum(li[i:]):
                c=i+1
        return c