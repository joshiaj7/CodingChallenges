from collections import deque
from typing import List

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        queue = deque()
        max_length = 1

        for num in sorted(set(nums)):
            if queue and num - queue[0] >= n:
                queue.popleft()

            queue.append(num)
            max_length = max(max_length, len(queue))

        return n - max_length
        