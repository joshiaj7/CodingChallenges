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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        ph = head
        ans = ListNode(0)
        pa = ans
        
        while ph:
            if not ph.next:
                pa.next = ph
                break
            elif ph.val == ph.next.val:
                rem = ph.val
                while ph.val == rem:
                    ph = ph.next
                    if not ph:
                        break
            else:
                pa.next = ListNode(ph.val)
                pa = pa.next
                ph = ph.next

        return ans.next