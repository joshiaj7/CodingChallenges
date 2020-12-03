"""
Space   : O(n)
Time    : O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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