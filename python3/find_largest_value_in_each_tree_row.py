from model import TreeNode
from typing import Optional, List

"""
Space   : O(n)
Time    : O(n)

DFS
"""

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        stack = [root]

        while stack:
            max_num = float('-inf')
            temp = []

            for node in stack:
                max_num = max(max_num, node.val)
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            ans.append(max_num)
            stack = temp
        
        return ans
