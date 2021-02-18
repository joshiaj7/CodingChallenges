# Space   : O(n)
# Time    : O(n)

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        temp = []
        n = len(A)

        if n < 3:
            return 0

        for i in range(1, n):
            temp.append(A[i] - A[i-1])

        count = 0
        for j in range(1, len(temp)):
            if temp[j] == temp[j-1]:
                count += 1
            else:
                count = 0
            ans += count

        return ans
