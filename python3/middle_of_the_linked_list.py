from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast.next:
            slow = slow.next
            fast = fast.next

            if fast and fast.next:
                fast = fast.next

        return slow
