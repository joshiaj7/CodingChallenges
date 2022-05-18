from collections import defaultdict

"""
Space   : O(n)
Time    : O(n + e)

Method:
Tarjan's algorithm
"""


class Solution(object):
    def criticalConnections(self, n, connections):
        def makeGraph(connections):
            graph = defaultdict(list)
            for conn in connections:
                graph[conn[0]].append(conn[1])
                graph[conn[1]].append(conn[0])
            return graph

        graph = makeGraph(connections)
        connections = set(map(tuple, (map(sorted, connections))))
        rank = [-2] * n

        def dfs(node, depth):
            if rank[node] >= 0:
                # visiting (0<=rank<n), or visited (rank=n)
                return rank[node]
            rank[node] = depth
            min_back_depth = n
            for neighbor in graph[node]:
                if rank[neighbor] == depth - 1:
                    # don't immmediately go back to parent. that's why i didn't choose -1 as the special value, in case depth==0.
                    continue
                back_depth = dfs(neighbor, depth + 1)
                if back_depth <= depth:
                    connections.discard(tuple(sorted((node, neighbor))))
                min_back_depth = min(min_back_depth, back_depth)
            # this line is not necessary. see the "brain teaser" section below
            rank[node] = n
            return min_back_depth

        # since this is a connected graph, we don't have to loop over all nodes.
        dfs(0, 0)
        return list(connections)
