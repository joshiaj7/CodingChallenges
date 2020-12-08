# Space   : O(n)
# Time    : O(n)

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        
        if n == 0:
            return 0
        
        ans = 0
        mods = [0] * 60
        memo = {}
        
        for x in time:
            mods[x % 60] += 1

        print(mods)
        for i in range(31):
            if i == 0 or i == 30:
                if mods[i] > 0:
                    if mods[i] not in memo:
                        temp = 0
                        for j in range(mods[i]):
                            temp += j
                            memo[j] = temp
                    ans += memo[mods[i]-1]
            else:
                ans += mods[i] * mods[60-i]
        
        return ans
        