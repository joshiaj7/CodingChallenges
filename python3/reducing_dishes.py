class Solution:
    """
    Space   : O(1)
    Time    : O(n log n + n^2)
    """
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans = 0

        satisfaction.sort()

        while satisfaction:
            count = 0
            for i, v in enumerate(satisfaction):
                count += (i+1) * v
            ans = max(ans, count)
            
            if satisfaction[0] < 0:
                satisfaction.pop(0)
            else:
                break

        return ans

    """
    Space   : O(1)
    Time    : O(n log n + n)
    """
    def maxSatisfactionBest(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = 0
        cur_sum = 0
        for val in satisfaction:
            cur_sum += val
            if (cur_sum < 0):
                break
            total += cur_sum
        return total
