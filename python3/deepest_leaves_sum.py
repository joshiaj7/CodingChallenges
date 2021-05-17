from .model import TreeNode

"""
Space : O(n)
Time  : O(n)
"""

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:        
        stack = [root]
        
        while stack:
            temp = []
            total = 0
            for i in stack:
                total += i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            if not temp:
                return total
            stack = temp
            
        return 0