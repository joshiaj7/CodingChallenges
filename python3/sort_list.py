"""
Space   : O(n)
Time    : O(n log n)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


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
