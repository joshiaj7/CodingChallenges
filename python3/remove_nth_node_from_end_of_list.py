from .model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
            
        if n == length:
            return head.next

        curr = head
        stop = length - n
        for i in range(stop - 1):
            curr = curr.next
        if not curr.next.next:
            curr.next = None
        else:
            curr.next = curr.next.next
        return head
