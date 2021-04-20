"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Space : O(n)
# Time  : O(n)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recursive(root):
            res = []
            
            if root:
                res.append(root.val)
                if root.children:
                    for node in root.children:
                        res += recursive(node)
                        
            return res
        
        return recursive(root)
        