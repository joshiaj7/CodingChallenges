from model import ListNode

"""
Space   : O(n)
Time    : O(n**2)
"""

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        mem = []

        point = head
        while point:
            mem.append(point.val)
            point = point.next

        n = len(mem)

        stack = []
        for i in range(n):
            stack.append(mem[i])
            j = len(stack) - 1
            while j > 0:
                if stack[j] < stack[j-1]:
                    temp = stack[j-1]
                    stack[j-1] = stack[j]
                    stack[j] = temp
                else:
                    break
                j -= 1

        ans = ListNode(stack[0])
        p = ans
        for i in range(1, len(stack)):
            p.next = ListNode(stack[i])
            p = p.next

        return ans
