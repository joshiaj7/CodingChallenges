from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        p = head
        a = ListNode(0)  # >= x
        p1 = a
        b = ListNode(0)  # < x
        p2 = b

        while p:
            if p.val >= x:
                p1.next = ListNode(p.val)
                p1 = p1.next
            else:
                p2.next = ListNode(p.val)
                p2 = p2.next
            p = p.next

        p2 = b
        while p2:
            if not p2.next:
                p2.next = a.next
                break
            p2 = p2.next

        return b.next
