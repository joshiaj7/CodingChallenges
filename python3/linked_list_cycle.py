from typing import Optional
from model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head

        while slow or fast:
            slow = slow.next
            fast = fast.next

            if fast:
                fast = fast.next

            if not slow or not fast:
                return False

            if slow == fast:
                if slow.next == fast.next:
                    break

        return True
