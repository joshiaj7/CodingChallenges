from .model import ListNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        temp = []
        p = head
        while p:
            temp.append(p.val)
            p = p.next

        while left < right:
            temp[left-1], temp[right-1] = temp[right-1], temp[left-1]
            left += 1
            right -= 1

        new_head = ListNode(temp[0])
        p = new_head
        for i in range(1, len(temp)):
            p.next = ListNode(temp[i])
            p = p.next

        return new_head
