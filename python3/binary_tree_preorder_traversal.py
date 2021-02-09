from model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getPreorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res.append(root.val)
            res += self.getPreorder(root.left)
            res += self.getPreorder(root.right)

        return res

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getPreorder(root)
