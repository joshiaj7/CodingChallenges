from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

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
