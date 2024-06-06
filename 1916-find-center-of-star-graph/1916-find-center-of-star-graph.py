class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        a = edges[0][0]
        b = edges[0][1]
        c = edges[1][0]
        d = edges[1][1]

        if(a==c or a==d):
            return a
        if(b==c or b==d):
            return b
        return -1