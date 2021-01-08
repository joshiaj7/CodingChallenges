"""
Space   : O(n)
Time    : O(n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        mem = []
        p = head
        
        while p:
            mem.append(p.val)
            p = p.next
            
        ans = ListNode(0)
        pans = ans
        
        for i in range(len(mem)):
            if i != len(mem)-n:
                pans.next = ListNode(mem[i])
                pans = pans.next
        
        return ans.next
