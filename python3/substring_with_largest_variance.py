"""
Space   : O(u)
Time    : O(u^2 * n)
u = length of unique char in s

Method:
kadane algorithm
"""


class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        unique = list(set(s))

        def count_variance(a, b, s):
            max_var = 0
            var = 0
            has_b = False
            first_b = False

            for c in s:
                if c == a:
                    var += 1
                elif c == b:
                    has_b = True

                    # shift right
                    if first_b and var >= 0:
                        first_b = False
                    # restart the subarray if the subarray only contains `b`s
                    elif var < 1:
                        first_b = True
                        var = -1
                    # var will always be >= 0
                    else:
                        var -= 1

                if has_b and var > max_var:
                    max_var = var

            return max_var

        for a in unique:
            for b in unique:
                if a == b:
                    continue
                variance = count_variance(a, b, s)
                ans = max(ans, variance)

        return ans
