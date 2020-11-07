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
    def getNumber(self, l: ListNode) -> int:
        num = ''
        while l:
            num += str(l.val)
            l = l.next

        return int(num)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = self.getNumber(l1) + self.getNumber(l2)
        ans = str(ans)

        n = len(ans)
        ll = ListNode(int(ans[0]))
        head = ll
        for i in range(1, n):
            head.next = ListNode(int(ans[i]))
            head = head.next

        return ll
