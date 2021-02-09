from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        stack = [(root, 10**6, -1)]

        while stack:
            node, minv, maxv = stack.pop()
            minv = min(minv, node.val)
            maxv = max(maxv, node.val)
            if not node.left and not node.right:
                ans = max(ans, abs(maxv - minv))
            if node.left:
                stack.append((node.left, minv, maxv))
            if node.right:
                stack.append((node.right, minv, maxv))

        return ans
