from model import TreeNode

"""
BFS Solution
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, [])]
        res = []
        ans = 0

        while stack:
            node, mem = stack.pop()
            if not node.left and not node.right:
                res.append(mem + [node.val])
                continue
            if node.left:
                stack.append((node.left, mem + [node.val]))
            if node.right:
                stack.append((node.right, mem + [node.val]))

        for item in res:
            d = {}
            for i in item:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            odds = 0
            for _, v in d.items():
                if v % 2 == 1:
                    odds += 1
            if odds <= 1:
                ans += 1

        return ans
