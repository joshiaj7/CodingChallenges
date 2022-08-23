from .model import ListNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        temp = []
        p = head
        while p:
            temp.append(p.val)
            p = p.next

        return temp == temp[::-1]
