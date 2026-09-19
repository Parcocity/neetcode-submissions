# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []

        def dfs(root: Optional[TreeNode]) -> None:
            nonlocal nums
            if root is None:
                return None
            
            dfs(root.left)
            
            nums.append(root.val)

            dfs(root.right)
        
        dfs(root)
        
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i+1]:
                return False
        
        return True
        
        
        
         



        