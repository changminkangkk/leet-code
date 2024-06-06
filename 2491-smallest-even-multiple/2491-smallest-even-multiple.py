class Solution:
    def smallestEvenMultiple(self, n):
        if n%2==0:
            return n
        else:
            i = n+n
            return i
        