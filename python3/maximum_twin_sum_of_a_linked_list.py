from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr, prev = slow, None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        while prev:
            ans = max(ans, prev.val + head.val)
            head = head.next
            prev = prev.next

        return ans
