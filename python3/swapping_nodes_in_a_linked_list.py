from .model import ListNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        p = head
        temp = []

        while p:
            temp.append(p.val)
            p = p.next

        temp[k-1], temp[~(k-1)] = temp[~(k-1)], temp[k-1]

        p = head
        i = 0
        while p:
            p.val = temp[i]
            i += 1
            p = p.next

        return head
