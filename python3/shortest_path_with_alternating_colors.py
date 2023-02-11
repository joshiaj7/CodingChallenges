"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = []
        for i in range(n):
            graph.append([[], []])

        # insert edges to graph
        for i, j in redEdges:
            graph[i][0].append(j)
        
        for i, j in blueEdges:
            graph[i][1].append(j)

        # init ans
        ans = [[0, 0]]
        for i in range(n-1):
            ans.append([n * 2, n * 2])

        # do bfs
        bfs = [[0, 0], [0, 1]]
        for i, color in bfs:
            for j in graph[i][color]:
                if ans[j][color] == n * 2:
                    ans[j][color] = ans[i][1 - color] + 1
                    bfs.append([j, 1 - color])

        # get result
        res = []
        for x in ans:
            m = min(x)
            if m < n * 2:
                res.append(m)
            else:
                res.append(-1)

        return res
