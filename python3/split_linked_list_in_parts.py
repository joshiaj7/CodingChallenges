from typing import Optional, List
from model import ListNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count the length of the linked list
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1

        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        ans = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)

        # Split up the list
        prev, curr = None, head
        for index, num in enumerate(ans):
            if prev:
                prev.next = None

            ans[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next

        return ans
