from model import TreeNode
class Solution:
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def countNodes(self, root: TreeNode) -> int:
        return len(self.inorderTraversal(root))