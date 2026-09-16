# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        dq = deque()
        dq.append([root])
        while dq:
            nodes = dq.popleft()
            res.append(nodes[-1].val)
            curr = []
            for node in nodes:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            if curr:
                dq.append(curr)
        return res
                



        