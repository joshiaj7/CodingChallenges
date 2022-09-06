from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def prune(root):
            if not root:
                return 0

            left = prune(root.left)
            if not left:
                root.left = None

            right = prune(root.right)
            if not right:
                root.right = None

            return left or right or root.val

        node_val = prune(root)
        return root if node_val else None
