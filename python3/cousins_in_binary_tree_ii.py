from collections import defaultdict
from typing import Optional
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        p = root
        stack = [[p, None]]

        while stack:
            temp = []

            d = defaultdict(int)
            total = 0
            for node, parent in stack:
                if node.left:
                    temp.append([node.left, node])
                if node.right:
                    temp.append([node.right, node])

                if parent:
                    d[parent] += node.val
                    total += node.val

            for node, parent in stack:
                node.val = total - d[parent]

            stack = temp

        return root
        