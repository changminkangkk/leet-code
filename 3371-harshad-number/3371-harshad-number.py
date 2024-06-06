class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        summ = sum([int(i) for i in str(x)])
        return summ if x%summ == 0 else -1