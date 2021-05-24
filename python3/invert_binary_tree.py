from .model import TreeNode

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        p = root
        
        if p:
            p.left, p.right = p.right, p.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root