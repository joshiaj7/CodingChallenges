from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, val):
            if root:
                if root.val >= val:
                    self.ans += 1
                dfs(root.left, max(val, root.val))
                dfs(root.right, max(val, root.val))

        self.ans = 0

        dfs(root, -float('inf'))
        return self.ans
