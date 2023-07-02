from typing import List

"""
Space   : O(n)
Time    : O(2^r * (n + r))
"""


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        r = len(requests)
        ans = 0

        def brute_force(mask):
            outdegrees = [0] * n
            indegrees = [0] * n

            for k in range(r):
                if (1 << k) & mask:
                    outdegrees[requests[k][0]] += 1
                    indegrees[requests[k][1]] += 1

            return sum(outdegrees) if outdegrees == indegrees else 0

        for i in range(1 << r):
            ans = max(ans, brute_force(i))

        return ans
