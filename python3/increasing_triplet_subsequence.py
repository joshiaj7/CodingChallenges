# Space : O(n)
# Time  : O(n)

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        mindp = [0] * n
        mindp[0] = -2147483648

        for i in range(n):
            if i == 0:
                mindp[i] = max(mindp[i], nums[i])
            else:
                mindp[i] = max(mindp[i-1], nums[i])

        maxdp = [0] * n
        maxdp[-1] = 2147483647

        for j in range(n-1, -1, -1):
            if j == n-1:
                maxdp[j] = min(maxdp[j], nums[j])
            else:
                maxdp[j] = min(maxdp[j+1], nums[j])

        # inc is for mindp, dec is for maxdp
        inc, dec = 0, 0
        for k in range(1, n):
            # check mindp
            if mindp[k] > mindp[k-1]:
                inc += 1

            # check maxdp
            if maxdp[~k] < maxdp[~k+1]:
                dec += 1

        return inc >= 2 or dec >= 2
