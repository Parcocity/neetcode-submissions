# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = []
        self.Count(root, res)
        return max(res)
        
        


    def Count(self, root: Optional[TreeNode], res: List[int]) -> int:
        if root is None:
            return -1
        count1 = 1+ self.Count(root.left, res)
        count2 = 1+ self.Count(root.right, res)
        res.append(count1+count2)
        return max(count1, count2)
        
