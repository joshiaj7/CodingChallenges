from typing import Optional
from model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        phead = head
        ans = ListNode(0)
        pans = ans

        total = 0
        while phead:
            if phead.val != 0:
                total += phead.val
            elif total > 0:
                newNode = ListNode(total)
                total = 0
                pans.next = newNode
                pans = pans.next 
                
            phead = phead.next

        return ans.next
        