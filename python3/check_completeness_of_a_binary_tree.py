from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        stack = [root]

        past_none = False
        while stack:
            temp = []
            for node in stack:
                if not node:
                    past_none = True
                    continue

                temp.append(node.left)
                temp.append(node.right)
                
                if past_none:
                    return False
                
            stack = temp

        return True        
