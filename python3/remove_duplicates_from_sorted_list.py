from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        ph = head
        ans = ListNode(0)
        pa = ans

        while ph:
            if not ph.next:
                pa.next = ph
                break

            while ph.val == ph.next.val:
                ph = ph.next
                if not ph.next:
                    break

            pa.next = ListNode(ph.val)
            pa = pa.next
            ph = ph.next

        return ans.next
