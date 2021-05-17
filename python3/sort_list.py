from .model import ListNode

"""
Space   : O(n)
Time    : O(n log n)
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        temp = []

        if not head:
            return head

        while head != None:
            temp.append(head.val)
            head = head.next

        temp = sorted(temp)

        ans = ListNode(temp[0])
        point = ans
        for i in temp[1:]:
            point.next = ListNode(i)
            point = point.next

        return ans
