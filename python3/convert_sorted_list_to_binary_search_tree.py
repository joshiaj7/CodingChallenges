from model import ListNode, TreeNode

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []

        p = head
        while p:
            vals.append(p.val)
            p = p.next

        def buildTree(vals):
            if not vals:
                return None

            mid = len(vals) // 2
            node = TreeNode(vals[mid])
            node.left = buildTree(vals[:mid])
            node.right = buildTree(vals[mid+1:])
            return node

        return buildTree(vals)
