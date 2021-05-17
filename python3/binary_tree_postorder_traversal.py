from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getPostorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res += self.getPostorder(root.left)
            res += self.getPostorder(root.right)
            res.append(root.val)

        return res

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getPostorder(root)
