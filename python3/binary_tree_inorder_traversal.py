from model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []

        if root:
            res += self.getInorder(root.left)
            res.append(root.val)
            res += self.getInorder(root.right)

        return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        return self.getInorder(root)
