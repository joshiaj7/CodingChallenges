from typing import List

"""
Space   : O(n^2)
Time    : O(2^n)
"""



class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        score_first = self.PredictTheWinnerInSituation(nums, 0, n-1, dp)
        score_total = sum(nums)
        return score_first >= score_total - score_first

    def PredictTheWinnerInSituation(self, nums, i, j, memo):
        # base case
        if i > j:
            return 0
        if i == j:
            return nums[i]
        if memo[i][j] != -1:
            return memo[i][j]
        
        # recursive case
        cur_score = max(nums[i] + min(self.PredictTheWinnerInSituation(nums, i+2, j, memo), self.PredictTheWinnerInSituation(nums, i+1, j-1, memo)), 
            nums[j] + min(self.PredictTheWinnerInSituation(nums, i, j-2, memo), self.PredictTheWinnerInSituation(nums, i+1, j-1, memo)))
        memo[i][j] = cur_score
        return cur_score
