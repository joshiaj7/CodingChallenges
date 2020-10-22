"""
Space   : O(n)
Time    : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = []
        stack = [(root, 1)]

        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls)
            if node.right:
                stack.append((node.right, ls+1))
            if node.left:
                stack.append((node.left, ls+1))

        return min(res)
