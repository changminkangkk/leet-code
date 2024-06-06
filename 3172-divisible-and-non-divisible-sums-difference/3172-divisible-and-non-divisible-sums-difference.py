class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div_by_m = []
        n_div_by_m = []
        for i in range(1,n+1):
            if((i%m) == 0):
                div_by_m.append(i)
            else:
                n_div_by_m.append(i)
        return sum(n_div_by_m) - sum(div_by_m)