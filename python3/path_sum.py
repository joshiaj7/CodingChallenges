from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""
class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            node, count = stack.pop()
            if not node.left and not node.right:
                if count + node.val == s:
                    return True
            if node.left:
                stack.append((node.left, count + node.val))
            if node.right:
                stack.append((node.right, count + node.val))

        return False
