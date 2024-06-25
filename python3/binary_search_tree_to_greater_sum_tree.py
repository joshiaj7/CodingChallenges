from model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.sum += root.val
            root.val = self.sum
            self.bstToGst(root.left)

        return root



        