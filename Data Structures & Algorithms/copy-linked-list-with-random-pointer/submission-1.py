"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToNew = {None: None}
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        
        ptr1 = head
        ptr2 = oldToNew[ptr1]
        while ptr1:
            if ptr1.next:

                ptr2.next = oldToNew[ptr1.next]
            else:
                ptr2.next = None
            if ptr1.random:
                ptr2.random = oldToNew[ptr1.random]
            else:
                ptr2.random = None
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return oldToNew[head]
        




        