class Solution():
    """This is not an OO problem and there is no need for an OO solution. Self is completely
    useless here and I cannot fathom why my time is being wasted with an object instead of a function."""
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest: int = max(set(candies))
        return [True if i + extraCandies >= greatest else False for i in candies]