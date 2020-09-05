# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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