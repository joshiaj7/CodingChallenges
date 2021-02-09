from model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

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
