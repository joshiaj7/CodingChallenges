from .model import NaryNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def postorder(self, root: NaryNode) -> List[int]:
        res = []

        if root:
            if root.children:
                for node in root.children:
                    res += self.postorder(node)
            res.append(root.val)

        return res
