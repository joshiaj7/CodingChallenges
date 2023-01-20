"""
Space   : O(2^n)
Time    : O(2^n)
"""

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = list()
        visited = set()
        n = len(nums)

        def dfs(index, leng, path):
            if index == leng:
                if len(path) > 1:
                    k = ",".join(map(str, path))
                    if k not in visited:
                        ans.append(path)
                        visited.add(k)
                        return 
            elif index < leng:
                # if path empty
                if not path:
                    dfs(index + 1, leng, path + [nums[index]])
                # if increasing
                elif path and path[-1] <= nums[index]:
                    dfs(index + 1, leng, path + [nums[index]])
                dfs(index + 1, leng, path)
            

        dfs(0, n, [])
        return ans
