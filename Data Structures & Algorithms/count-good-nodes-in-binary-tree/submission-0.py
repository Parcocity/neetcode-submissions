# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        prev = -101
        def Count(root: TreeNode, prev: int) -> int:
            if root is None:
                return 0
            if root.val >= prev:
                prev = root.val
                return 1 + Count(root.left, prev) + Count(root.right, prev)
            else:
                return Count(root.left, prev) + Count(root.right, prev)
        
        return Count(root, prev)
            
                
        