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

        left, right = None, None
        if list1.val <= list2.val:
            left = list1
            right = list2
        else:
            left = list2
            right = list1

        # left = min(list1, list2, key=lambda x:x.val)
        # right = max(list1, list2, key=lambda x:x.val)

        head = left
        curr = left
        left = left.next
        while curr:
            if left is None:
                curr.next = right
                break
            elif right is None:
                curr.next = left
                break
            elif left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next
        
        return head