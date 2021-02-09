from model import TreeNode


"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, [])]
        ans = 10**10

        while stack:
            node, prevs = stack.pop()
            if prevs:
                for prev in prevs:
                    ans = min(ans, abs(prev - node.val))
            if node.left:
                stack.append((node.left, prevs + [node.val]))
            if node.right:
                stack.append((node.right, prevs + [node.val]))

        return ans
