from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        skip = (n // 2) - 1
        p = head
        while skip > 0:
            skip -= 1
            p = p.next

        p.next = p.next.next
        return head
