"""
Space   : O(n)
Time    : O(n**2)
Divide and conquer
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k <= 1:
            return len(s)

        stack = [s]
        ans = 0

        while stack:
            w = stack.pop()
            if len(w) < k:
                continue

            count = {}
            for l in w:
                if l not in count:
                    count[l] = 1
                else:
                    count[l] += 1

            target = ''
            for key, val in count.items():
                if val < k:
                    target = key
                    break

            if len(target) > 0:
                stack += w.split(target)
            else:
                ans = max(ans, len(w))

        return ans
