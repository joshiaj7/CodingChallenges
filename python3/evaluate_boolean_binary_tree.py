from model import TreeNode
from typing import Optional

"""
Space   : O(1)
Time    : O(n)
"""

class Solution:    
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluate(root):
            if root.left and root.right:
                left = evaluate(root.left)
                curr = root.val
                right = evaluate(root.right)

                if curr == 2:
                    return left or right
                return left and right

            return root.val
    
        return evaluate(root)

        