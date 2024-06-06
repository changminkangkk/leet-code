# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:    
    def getTargetCopy(self, node1: TreeNode, node2: TreeNode, target: TreeNode) -> TreeNode:        
        if not node1 or target == node1:  # if node1 is null, node2 will also be null
            return node2
        
        return self.getTargetCopy(node1.left, node2.left, target) or self.getTargetCopy(node1.right, node2.right, target)        