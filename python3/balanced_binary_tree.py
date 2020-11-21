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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def checkBalanced(root):
            nonlocal balanced
            if not root:
                return 0

            l = checkBalanced(root.left) + 1
            r = checkBalanced(root.right) + 1

            if abs(l - r) > 1:
                balanced = False

            return max(l, r)

        balanced = True
        checkBalanced(root)
        return balanced
