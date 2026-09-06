# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            if list1.val > list2.val:
                head = list2
                ptr1 = head.next
                ptr2 = list1
            else:
                head = list1
                ptr1 = head.next
                ptr2 = list2

        curr = head
        while (ptr1 is not None and ptr2 is not None):
            if ptr1.val <= ptr2.val:
                curr.next = ptr1
                ptr1 = ptr1.next
                curr = curr.next
            else:
                curr.next = ptr2
                ptr2 = ptr2.next
                curr = curr.next
        if ptr1 is None:
            curr.next = ptr2
        if ptr2 is None:
            curr.next = ptr1

        return head







        

        

        