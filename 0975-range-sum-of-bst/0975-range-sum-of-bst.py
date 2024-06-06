class Solution:
    def rangeSumBST(self, r: Optional[TreeNode], l: int, h: int) -> int:
        return (f:=lambda n:f(n.left)+n.val*(l<=n.val<=h)+f(n.right) if n else 0)(r)