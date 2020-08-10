# leetcode

class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n < 2:
        #     return n
        
        ans, count = 0, 0
        add = 1

        while count < n:
            # print("count : {}, add: {}, ans: {}".format(count, add, ans))
            count += add
            add += 1
            ans += 1
            
        if count > n:
            ans -= 1
        
        # print("ans : {}".format(ans))
        
        return ans