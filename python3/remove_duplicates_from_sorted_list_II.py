from model import ListNode


"""
Space   : O(1)
Time    : O(n)
"""

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