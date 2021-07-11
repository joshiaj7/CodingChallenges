from .model import NaryNode

# Space : O(n)
# Time  : O(n)


class Solution:
    def preorder(self, root: NaryNode) -> List[int]:
        def recursive(root):
            res = []

            if root:
                res.append(root.val)
                if root.children:
                    for node in root.children:
                        res += recursive(node)

            return res

        return recursive(root)
