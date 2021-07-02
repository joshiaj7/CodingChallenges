# Space : O(2^n)
# Time  : O(2^n)

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        ans.append(0)

        for i in range(1, n+1):
            prev_len = len(ans)
            mask = 1 << (i-1)
            for j in range(prev_len, 0, -1):
                ans.append(mask + ans[j-1])
        return ans
