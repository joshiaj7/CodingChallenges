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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la, lb = 0, 0
        pa, pb = headA, headB
        
        while pa:
            la += 1
            pa = pa.next
            
        while pb:
            lb += 1
            pb = pb.next
        
        pa, pb = headA, headB
        
        if la > lb:
            dif = la - lb
            while dif > 0:
                pa = pa.next
                dif -= 1                
        else:
            dif = lb - la
            while dif > 0:
                pb = pb.next
                dif -= 1    
        
        while pa:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next

            
        return None