from typing import Optional
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [root]

        while stack:
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if not temp:
                return stack[0].val

            stack = temp

        return 0






        