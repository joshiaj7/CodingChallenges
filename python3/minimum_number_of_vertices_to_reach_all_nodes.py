"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = []

        indegrees = set([v for u, v in edges])
        for i in range(n):
            if i not in indegrees:
                ans.append(i)

        return ans
