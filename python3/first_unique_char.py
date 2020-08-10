# leetcode

class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = -1
        dup = []
        
        for idx in range(len(s)):
            if s[idx] in s[idx+1:]:
                dup.append(s[idx])
                continue
            elif s[idx] not in s[idx+1:] and s[idx] not in dup:
                ans = idx
                break
                
        return ans
        