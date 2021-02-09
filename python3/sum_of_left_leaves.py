from model import TreeNode

# Space : O(n)
# Time : O(n)
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [root]
        ans = 0

        while stack:
            node = stack.pop()

            if node.left:
                if not node.left.left and not node.left.right:
                    ans += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return ans
