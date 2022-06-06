
from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        na, nb = 0, 0
        pa, pb = headA, headB

        while pa:
            pa = pa.next
            na += 1

        while pb:
            pb = pb.next
            nb += 1

        pa, pb = headA, headB

        while na > nb:
            pa = pa.next
            na -= 1

        while nb > na:
            pb = pb.next
            nb -= 1

        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next

        return None
