from .model import TreeNode
from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans = []
        
        def tuplify(root):
            if not root:
                return "null"
            tup = "{},{},{}".format(root.val, tuplify(root.left), tuplify(root.right))
            nodes[tup].append(root)
            return tup

        nodes = defaultdict(list)
        tuplify(root)
        
        for _, v in nodes.items():
            if len(v) > 1:
                ans.append(v[0])
        
        return ans
