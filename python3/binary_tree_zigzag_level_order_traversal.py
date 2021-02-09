from model import TreeNode

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:

    def getDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        l = self.getDepth(root.left) + 1
        r = self.getDepth(root.right) + 1

        return max(l, r)

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        maxdep = self.getDepth(root)

        for _ in range(maxdep):
            ans.append([])

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop(0)
            ans[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        direct = "l"
        for j in range(maxdep):
            if direct == "l":
                direct = "r"
                continue
            ans[j] = ans[j][::-1]
            direct = "l"

        return ans
