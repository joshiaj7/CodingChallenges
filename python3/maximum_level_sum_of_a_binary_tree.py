from typing import Optional
from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        h = {}
        stack = [root]

        level = 1
        while stack:
            temp = []
            total = 0
            for node in stack:
                total += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            h[level] = total
            level += 1
            stack = temp

        mval = -1 * 10**5
        ans = 0 
        for k, v in h.items():
            if v > mval:
                mval = v
                ans = k

        return ans
