"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        if not odd.next:
            return odd

        even = head.next
        po, pe = odd, even
        counter = 1
        while po.next and pe.next:
            if counter % 2 == 1:
                po.next = po.next.next
                po = po.next
            else:
                pe.next = pe.next.next
                pe = pe.next
            counter += 1

        if po.next:
            po.next = None
        if pe.next:
            pe.next = None

        po.next = even
        return odd


