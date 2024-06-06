class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0] * 2
        idx = mxCnt = 0
        for i in range(len(mat)):
            cnt = 0
            for ele in mat[i]:
                if ele == 1:
                    cnt += 1
            if cnt > mxCnt:
                idx = i
                mxCnt = cnt
        ans[0] = idx
        ans[1] = mxCnt
        return ans