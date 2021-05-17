from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        ans = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans
