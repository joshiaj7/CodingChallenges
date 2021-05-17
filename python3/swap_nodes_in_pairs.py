from .model import ListNode

"""
Space   : O(1)
Time    : O(n/2)
"""

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        point = head

        while point:
            temp = point.val

            if not point.next:
                break
            point.val = point.next.val
            point.next.val = temp

            point = point.next.next

        return head
