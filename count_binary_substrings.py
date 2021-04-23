# Space : O(1)
# Time : O(n)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        last = s[0]
        one = 1 if s[0] == '1' else 0
        zero = 1 if s[0] == '0' else 0
        n = len(s)
        
        for i in range(1, n):
            if s[i] != last:
                ans += min(one, zero)
                if s[i] == '0':
                    zero = 1
                else:
                    one = 1
            else:
                if s[i] == '0':
                    zero += 1
                else:
                    one += 1
            last = s[i]

        ans += min(one, zero)
        
        return ans