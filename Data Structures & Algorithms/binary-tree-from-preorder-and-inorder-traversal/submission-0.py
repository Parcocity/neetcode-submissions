# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}
        for index, val in enumerate(inorder):
            hashmap[val] = index
            
        ptr = 0
        def dfs(left: int, right: int) -> Optional[TreeNode]:
            nonlocal ptr
            if left > right:
                return None
            
            root = preorder[ptr]
            ptr += 1

            node = TreeNode(root)

            mid = hashmap[root]

            node.left = dfs(left, mid - 1)
            node.right = dfs(mid + 1, right)

            return node
        
        return dfs(0, len(inorder) - 1)



        



        