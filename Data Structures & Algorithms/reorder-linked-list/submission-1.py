# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        curr = slow.next
        slow.next = None
        prev = None

        while (curr):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        ptr1 = head
        ptr2 = prev
        curr = ptr1

        while ptr2:
            temp1 = ptr1.next
            temp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1 = temp1
            ptr2 = temp2

        
            






