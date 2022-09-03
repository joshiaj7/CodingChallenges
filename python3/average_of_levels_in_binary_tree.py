from .model import TreeNode

"""
Space	: O(n)
Time	: O(n)
"""

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        ans = []
        stack = [root]
        
        while stack:
            val = 0
            temp = []
            for node in stack:
                val += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                
            ans.append(val / len(stack))
            
            stack = temp
        
        return ans
