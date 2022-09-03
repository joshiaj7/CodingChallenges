"""
Space   : O(n!)
Time    : O(n!)
"""


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(n, k, path):
            if len(path) == 0:
                for i in range(1, 10):
                    dfs(n, k, path + str(i))
            elif len(path) < n:
                last = int(path[-1])
                if k == 0:
                    dfs(n, k, path + path[-1])
                else:
                    # minus
                    if last-k >= 0:
                        dfs(n, k, path + str(last-k))
                    # plus
                    if last+k <= 9:
                        dfs(n, k, path + str(last+k))
            elif len(path) == n:
                ans.append(int(path))

        ans = []
        dfs(n, k, '')
        return ans
