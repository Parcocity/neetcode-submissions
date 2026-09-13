# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        return self.maxDepthCount(root, res)
    
    def maxDepthCount(self, root: Optional[TreeNode], count: int) -> int:
        if root is None:
            return count
        return max(self.maxDepthCount(root.left, count+1), self.maxDepthCount(root.right, count+1))
        
        

        