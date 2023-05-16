from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head
    
        ans = ListNode()
        p = ans

        while True:
            p1, p2 = head, head.next
            if p1 and p2:
                tmp = p2.next

                p1.next = None
                p2.next = None

                p.next = p2
                p.next.next = p1
                
                head = tmp
                p = p.next.next
            elif p1 and not p2:
                p.next = p1
                break
            
            if not head:
                break


        return ans.next
