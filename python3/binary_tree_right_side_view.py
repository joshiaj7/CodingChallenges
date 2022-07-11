from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            ans.append(stack[-1].val)
            temp = []
            for node in stack:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                    
            stack = temp
        
        return ans
