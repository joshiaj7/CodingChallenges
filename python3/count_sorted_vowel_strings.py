class Solution:
    def countVowelStringsMath(self, n: int) -> int:
        """
        Mathematical approach
        Space   : O(1)
        Time    : O(1)
        """
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24

    def countVowelStringsDP(self, n: int) -> int:
        """
        DP approach
        Space   : O(5)
        Time    : O(n)
        """

        if n == 1:
            return 5

        dp = [1, 1, 1, 1, 1]
        count = 5

        while n > 1:
            temp = [count]
            for i in range(4):
                temp.append(temp[-1]-dp[i])
            count = sum(temp)
            dp = temp
            n -= 1

        return count
