from .model import TreeNode

from collections import defaultdict

"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        stack = [(root, 0)]
        minv, maxv = 0, 0

        while stack:
            stemp = []
            dtemp = defaultdict(list)
            for node, pos in stack:
                minv = min(minv, pos)
                maxv = max(maxv, pos)

                dtemp[pos].append(node.val)

                if node.left:
                    stemp.append((node.left, pos - 1))
                if node.right:
                    stemp.append((node.right, pos + 1))

            for k, v in dtemp.items():
                d[k].extend(sorted(v))

            stack = stemp

        ans = []
        for i in range(minv, maxv+1):
            ans.append(d[i])

        return ans
