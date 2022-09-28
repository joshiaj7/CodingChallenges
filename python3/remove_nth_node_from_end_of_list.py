from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
