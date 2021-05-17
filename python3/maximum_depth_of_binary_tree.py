from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.getDepth(root.left) + 1
        r = self.getDepth(root.right) + 1

        return max(l, r)

    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root)
