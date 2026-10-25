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
        # for _ in range(3):
            print(s.val, f.val)
            t = f.next
            f.next = s
            s = f
            f = t
            
        print(s.val)
        return s
