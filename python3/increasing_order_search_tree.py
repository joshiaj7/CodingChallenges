from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def getInorder(self, root) -> List[int]:
        res = []
        
        if root:
            res += self.getInorder(root.left)
            res.append(root.val)
            res += self.getInorder(root.right)
            
        return res
    
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        vals = self.getInorder(root)

        # create tree
        ans = TreeNode()
        head = ans
        
        for i in vals:
            head.right = TreeNode(i)
            head = head.right
        
        return ans.right