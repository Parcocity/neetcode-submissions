# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeRecursion(root)
        return root

    def invertTreeRecursion(self, root) -> None:
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTreeRecursion(root.left)
        self.invertTreeRecursion(root.right)
        