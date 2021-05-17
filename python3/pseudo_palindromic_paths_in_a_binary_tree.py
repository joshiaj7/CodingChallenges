from .model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        pals = []
        stack = [(root, [])]

        while stack:
            node, mem = stack.pop()
            if not node.left and not node.right:
                pals.append(mem + [node.val])
            if node.left:
                stack.append((node.left, mem + [node.val]))
            if node.right:
                stack.append((node.right, mem + [node.val]))

        for item in pals:
            d = {}
            odds = 0
            for i in item:
                if i not in d:
                    d[i] = 1
                    odds += 1
                else:
                    d[i] += 1
                    if d[i] % 2 == 0:
                        odds -= 1
                    else:
                        odds += 1
            if odds <= 1:
                ans += 1

        return ans
