from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        h1 = head
        h2 = head

        cyclical = True
        while h1 or h2:
            h1 = h1.next
            h2 = h2.next
            if h2:
                h2 = h2.next

            if not h1 or not h2:
                cyclical = False
                break

            if h1.val == h2.val and h1.next and h2.next and h1.next.val == h2.next.val:
                break
                
            
        if not cyclical:
            return None

        point = head
        while point:
            if point.val == h1.val and point.next and h1.next and point.next.val == h1.next.val:
                return point

            h1 = h1.next
            point = point.next
