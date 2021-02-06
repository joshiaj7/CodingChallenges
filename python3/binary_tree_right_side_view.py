"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [root]

        while stack:
            temp = []
            for idx in range(len(stack)):
                if not stack[idx]:
                    continue
                if idx == len(stack)-1:
                    ans.append(stack[idx].val)
                if stack[idx].left:
                    temp.append(stack[idx].left)
                if stack[idx].right:
                    temp.append(stack[idx].right)

            stack = temp

        return ans
