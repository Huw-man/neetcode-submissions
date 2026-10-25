# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        s = head
        f = head.next
        s.next = None
        while f:
            t = f.next
            f.next = s
            s = f
            f = t
            
        return s
