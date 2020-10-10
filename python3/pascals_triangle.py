"""
Space   : O(nk)
Time    : O(nk)
"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        if numRows == 0:
            return ans

        ans.append([1])

        if numRows == 1:
            return ans

        ans.append([1, 1])

        if numRows == 2:
            return ans

        for i in range(3, numRows+1):
            temp = []
            for idx in range(i):
                if (idx == 0) or (idx == i-1):
                    temp.append(1)
                    continue
                temp.append(ans[i-2][idx-1] + ans[i-2][idx])
            ans.append(temp)

        return ans
