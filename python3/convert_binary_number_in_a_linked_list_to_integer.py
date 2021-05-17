from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0

        ans = ''

        while head:
            ans += str(head.val)
            head = head.next

        print(ans)
        return int(ans, 2)
