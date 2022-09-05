"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        ans = []
        stack = [root]

        while stack:
            temp = []
            line = []
            for node in stack:
                line.append(node.val)

                if node.children:
                    temp += node.children

            ans.append(line)
            stack = temp

        return ans
