# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        nth = length - n
        if nth == 0:
            return head.next
    
        curr = head
        while nth-1 > 0:
            curr = curr.next
            nth -= 1
        curr.next = curr.next.next

        return head
        
