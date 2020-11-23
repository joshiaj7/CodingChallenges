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
    def rob(self, root: TreeNode) -> int:
        """
        Best possible solution
        Easy to understand
        """
        def recurse(node):
            if not node:
                return (0, 0)

            left = recurse(node.left)
            right = recurse(node.right)

            rob = node.val + left[1] + right[1]
            no_rob = max(left) + max(right)

            return (rob, no_rob)

        return max(recurse(root))
