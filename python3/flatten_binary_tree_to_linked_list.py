from .model import TreeNode

# Space : O(n)
# Time  : O(n)

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def preorder(root):
            res = []
            
            if root:
                res.append(root.val)
                res += preorder(root.left)
                res += preorder(root.right)
                
            return res
        
        temp = preorder(root)
        n = len(temp)
        p = root

        for i in range(n):
            if i == 0:
                p.val = temp[i]
            else:
                p.right = TreeNode(temp[i])
                p.left = None
                p = p.right
