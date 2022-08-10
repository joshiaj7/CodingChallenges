from .model import TreeNode

"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build_bst(a):
            if not a:
                return None
            mid = len(a) // 2
            root = TreeNode(a[mid])
            root.left = build_bst(a[:mid])
            root.right = build_bst(a[mid+1:])

            return root

        return build_bst(nums)
