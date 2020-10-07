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
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        temp = []

        while head != None:
            temp.append(head.val)
            head = head.next

        n = len(temp)

        if k > n:
            print(k % n)
            k %= n

        new_temp = temp[-k:] + temp[:-k]

        ans = ListNode(new_temp[0])
        pointer = ans
        for i in range(1, n):
            pointer.next = ListNode(new_temp[i])
            pointer = pointer.next

        return ans
