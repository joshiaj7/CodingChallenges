from model import TreeNode

"""
Space   : O(n)
Time    : O(n*edges)
"""

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 10**10

        stack = [(root, [])]

        while stack:
            node, prev = stack.pop(0)
            if prev:
                for i in prev:
                    ans = min(ans, abs(i - node.val))
            if node.left:
                stack.append((node.left, prev + [node.val]))
            if node.right:
                stack.append((node.right, prev + [node.val]))

        return ans
