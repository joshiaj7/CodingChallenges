from typing import List

"""
Space   : O(n)
Time    : O(2^r * (n + r))
"""


class Solution:
    # masking
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

    # backtrack
    def helper(self, start, requests, indegree, n, count):
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take 
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Not-take
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequestsBacktrack(self, n, requests):
        self.ans = 0
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans
