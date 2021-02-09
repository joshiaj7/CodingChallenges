from model import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNodes(self, head, res) -> list():
        if head:
            res.append(head.val)
            self.getNodes(head.next, res)
        return res
    
    def reverseList(self, head: ListNode) -> ListNode:
        vals = self.getNodes(head, [])
        ptr = head
        
        for i in range(len(vals)-1, -1, -1):
            ptr.val = vals[i]
            ptr = ptr.next

        return head