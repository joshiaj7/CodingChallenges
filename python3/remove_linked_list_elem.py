# leetcode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNode(self, head, key):  
        temp = head
        
        while temp:
            if temp.val == key:
                temp = temp.next
            else:
                break
        head = temp

        while temp:  
            if temp.val == key:  
                prev.next = temp.next
            else:
                prev = temp  
            temp = temp.next

        return head
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = self.deleteNode(head, val)
        return res
        
        