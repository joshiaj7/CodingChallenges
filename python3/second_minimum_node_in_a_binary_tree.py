from .model import TreeNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        s = [root]
        ans = -1
        minv = None

        while s:
            node = s.pop(0)

            if not minv:
                minv = node.val
            elif (ans == -1 or node.val < ans) and node.val != minv:
                if node.val < minv:
                    minv, ans = node.val, minv
                else:
                    ans = node.val

            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

        return ans
