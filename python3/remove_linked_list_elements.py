from model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def deleteNode(self, head, key):  
        temp = head
        
        while temp:
            if temp.val == key:
                temp = temp.next
            else:
                break
        head = temp
        prev = head

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
        
        