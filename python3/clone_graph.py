from model import GraphNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def cloneGraph(self, node: GraphNode) -> GraphNode:
        if not node:
            return None
        
        graph_map = {}

        def dfs(cur):
            if cur.val in graph_map:
                return graph_map[cur.val] 

            new_node = GraphNode(cur.val, [])
            graph_map[cur.val] = new_node
            for neigh in cur.neighbors:
                new_node.neighbors.append(dfs(neigh))

            return new_node

        return dfs(node)
