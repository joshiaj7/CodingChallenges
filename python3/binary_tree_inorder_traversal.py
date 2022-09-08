from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []
        
        if root:
            res += self.inorderTraversal(root.left)
            res.append(root.val)
            res += self.inorderTraversal(root.right)
            
        return res
