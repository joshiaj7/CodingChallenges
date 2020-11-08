"""
Space   : O(1)
Time    : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


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
