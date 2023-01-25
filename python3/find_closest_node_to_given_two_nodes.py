"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        graph = {}

        for i in range(n):
            graph[i] = edges[i]

        d1, d2 = {}, {}
        i = 0
        while node1 not in d1 and node1 != -1:
            d1[node1] = i
            node1 = graph[node1]
            i += 1

        i = 0
        while node2 not in d2 and node2 != -1:
            d2[node2] = i
            node2 = graph[node2]
            i += 1

        step = float('inf')
        ans = -1
        for k, v in d1.items():
            if k in d2 and max(v, d2[k]) <= step:
                req = max(v, d2[k])
                if req < step:
                    step = req
                    ans = k
                elif step == req:
                    ans = min(ans, k)

        return ans
