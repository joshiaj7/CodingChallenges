from .model import TreeNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        s = set()
        q = [root]

        while q:
            node = q.pop()

            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False
