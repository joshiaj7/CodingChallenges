from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None

        h1 = head
        h2 = head

        while h1 or h2:
            h1 = h1.next
            h2 = h2.next
            if h2:
                h2 = h2.next
            if not h2 or not h1:
                return False

            if h1.val == h2.val:
                if h1.next.val == h2.next.val:
                    break

        return True
