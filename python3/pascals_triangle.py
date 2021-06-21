"""
Space   : O(nk)
Time    : O(nk)
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1, numRows+1):
            temp = []
            for j in range(1, i+1):
                if (j == 1) or (j == i):
                    temp.append(1)
                else:
                    temp.append(ans[i-2][j-2] + ans[i-2][j-1])
            ans.append(temp)

        return ans
