from .model import RandListNode

"""
Space   : O(2n)
Time    : O(2n)
"""


class Solution:
    def copyRandomList(self, head: RandListNode) -> RandListNode:
        p = head

        # create interweaved list
        while p:
            # save value to next creation
            value = p.val
            temp = p.next

            # insert copied current node
            p.next = RandListNode(value)
            p = p.next

            # point back to original next
            p.next = temp
            p = p.next

        # migrate random node
        p = head
        while p:
            if p.random:
                # save rand
                rand = p.random

                # insert rand to new rand
                p = p.next
                p.random = rand.next
                p = p.next
            else:
                p = p.next.next

        # create new node
        ans = RandListNode(0)
        a = ans
        p = head
        while p:
            # move next
            p = p.next

            # insert to ans
            a.next = p

            # move to next element
            a = a.next
            p = p.next

        return ans.next
