from model import TreeNode

# Space : O(n)
# Time  : O(n)

class Solution:
    def getInorder(self, root: TreeNode) -> List[int]:
        res = []
        
        if root:
            res += self.getInorder(root.left)
            res.append(root.val)
            res += self.getInorder(root.right)
            
        return res
    
    
    def isValidBST(self, root: TreeNode) -> bool:
        vals = self.getInorder(root)
        
        for i in range(1, len(vals)):
            if vals[i] <= vals[i-1]:
                return False
        
        return True