from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        n = 0

        while p:
            p = p.next
            n += 1

        s = k - 1
        e = n - k
        p1, p2 = head, head

        while s > 0 or e > 0:
            if s > 0:
                p1 = p1.next
                s -= 1
            if e > 0:
                p2 = p2.next 
                e -= 1

        p1.val, p2.val = p2.val, p1.val               
        return head
