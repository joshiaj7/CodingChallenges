from .model import TreeNode

# Space : O(n)
# Time  : O(n)

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        stack = [(root, [])]

        while stack:
            temp = []
            ancs = []
            for n, a in stack:
                if n.left:
                    temp.append((n.left, a + [n]))
                if n.right:
                    temp.append((n.right, a + [n]))
                ancs.append(a + [n])

            if not temp:
                break
            stack = temp

        if len(ancs) == 1:
            return ancs[0][-1]

        i = 0
        while i < len(ancs[0]):
            prev = ancs[0][i]
            for j in range(1, len(ancs)):
                if prev != ancs[j][i]:
                    return ancs[j][i-1]
            i += 1

        return TreeNode()
