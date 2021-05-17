from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    # preorder transversal
    def getLeaf(self, root) -> List[int]:
        ans = []
        if root: 
            ans += self.getLeaf(root.left) 
            ans.append(root.val)
            ans += self.getLeaf(root.right)
        return ans
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        
        value1 = self.getLeaf(root1)
        value2 = self.getLeaf(root2)
        
        ans.extend(value1)
        ans.extend(value2)
        
        return sorted(ans)