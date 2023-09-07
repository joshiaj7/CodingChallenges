from model import ListNode
from typing import Optional

# Space : O(n)
# Time  : O(n)


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        ans = ListNode(0)
        ans.next = head
        pre = ans

        for i in range(left - 1):
            pre = pre.next
        
        # reverse the [left, right] nodes
        reverse = None
        cur = pre.next
        for i in range(right - left + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return ans.next
