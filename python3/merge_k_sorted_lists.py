"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = 0
        ans = ListNode(0)
        p = ans
        temp = []

        for x in lists:
            while x:
                temp.append(x.val)
                x = x.next
                n += 1

        temp.sort()

        for i in range(n):
            p.next = ListNode(temp[i])
            p = p.next

        return ans.next
