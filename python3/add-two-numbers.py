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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        v1, v2 = 0, 0
        
        mul = 1
        while p1:
            v1 = v1 + (p1.val * mul)
            mul *= 10
            p1 = p1.next
        
        mul = 1
        while p2:
            v2 = v2 + (p2.val * mul)
            mul *= 10
            p2 = p2.next
        
        tot = str(v1 + v2)
        ans = ListNode(0)
        point = ans
        
        for i in range(len(tot)-1, -1, -1):
            point.next = ListNode(int(tot[i]))
            point = point.next
        
        return ans.next