from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(root):
            res = []
            
            if root:
                res += inorder(root.left)
                if not root.left and not root.right:
                    res.append(root.val)
                res += inorder(root.right)

            return res
            
        return inorder(root1) == inorder(root2)
