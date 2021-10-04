from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head
        
        l = 0
        while p1:
            l += 1
            p1 = p1.next
            
        l //= 2
        while l > 0:
            p2 = p2.next
            l -= 1
    
        return p2
        