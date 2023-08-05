from functools import lru_cache
from typing import List, Optional
from model import TreeNode

"""
Space   : O(n*Cn)
Time    : O(Cn)

Cn = catalan number
"""

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        @lru_cache(None)
        def generateTree(left, right):
            if left > right: 
                return [None]

            if left == right:
                return [TreeNode(left)]

            ans = []
            for root in range(left, right+1):
                left_nodes = generateTree(left, root-1)
                right_nodes = generateTree(root+1, right)
                for left_node in left_nodes:
                    for right_node in right_nodes:
                        root_node = TreeNode(root, left_node, right_node)
                        ans.append(root_node)

            return ans

        return generateTree(1, n)
