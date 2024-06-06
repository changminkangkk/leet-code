# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # null check && considering serching value is not available in the tree
        if not root:
            return
        # considering the serching value is in right side of the tree
        if val>root.val:
            return self.searchBST(root.right,val)
        # considering the serching value is in right side of the tree
        elif val<root.val:
            return self.searchBST(root.left,val)
        #return if value exist 
        return root       
        