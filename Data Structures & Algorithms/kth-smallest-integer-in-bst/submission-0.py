# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num = -1
        count = 1

        def dfs(root: Optional[TreeNode], k: int) -> None:
            nonlocal num
            nonlocal count
            if root is None:
                return None

            dfs(root.left, k)

            if k == count:
                num = root.val
            count += 1

            dfs(root.right, k)
        
        dfs(root, k)
        return num
        

        