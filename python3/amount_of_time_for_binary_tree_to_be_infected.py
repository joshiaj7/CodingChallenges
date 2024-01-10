from model import TreeNode
from collections import defaultdict
from typing import Optional

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0

        g = defaultdict(list)
        stack = [root]

        # build graph
        while stack:
            temp = []

            for node in stack:
                if node.left:
                    g[node.val].append(node.left.val)
                    g[node.left.val].append(node.val)
                    temp.append(node.left)

                if node.right:
                    g[node.val].append(node.right.val)
                    g[node.right.val].append(node.val)
                    temp.append(node.right)
                    
            stack = temp


        # traverse
        visited = set()
        layer = [start]
        while layer:
            temp = []

            for cur in layer:
                for neighbor in g[cur]:
                    if neighbor not in visited:
                        temp.append(neighbor)
                visited.add(cur)

            if temp:
                ans += 1            
    
            layer = temp
            
        return ans

