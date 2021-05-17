from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        total = 0

        def check(root: TreeNode) -> int:
            nonlocal total

            if not root:
                return 0

            l = check(root.left)
            r = check(root.right)
            tilt = abs(l - r)
            total += tilt

            return root.val + l + r

        check(root)

        return total
