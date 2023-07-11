from typing import List
from collections import defaultdict
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        graph = defaultdict(list)

        def build_graph(node):
            if node:
                if node.left:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                if node.right:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)

                build_graph(node.left)
                build_graph(node.right)

        build_graph(root)

        visited = set()
        def dfs(val, step):
            visited.add(val)
            if step == k:
                ans.append(val)
                return
            
            for i in graph[val]:
                if i in visited:
                    continue
                dfs(i, step + 1)
        

        dfs(target.val, 0)
        return ans
