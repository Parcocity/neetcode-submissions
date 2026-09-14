# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = []
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root is None:
                return -1
            
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)

            res.append(left - right)
            return max(left, right)
        
        dfs(root)
        for i in res:
            if i < -1 or i > 1:
                return False
        return True



        