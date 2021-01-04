"""
Space   : O(1)
Time    : O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        ans = ListNode(0)
        pans = ans
    
        while p1 and p2:
            if p1.val < p2.val:
                pans.next = ListNode(p1.val)
                p1 = p1.next
            else:
                pans.next = ListNode(p2.val)
                p2 = p2.next
            pans = pans.next
        
        if p1:
            pans.next = p1

        if p2:
            pans.next = p2
        
        return ans.next