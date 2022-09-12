"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        
        tokens.sort()
        
        score = 0
        while tokens:
            while tokens and power >= tokens[0]:
                t = tokens.pop(0)
                power -= t
                score += 1
            
            ans = max(ans, score)
            
            if not tokens:
                break
                
            if score and power < tokens[0]:
                power += tokens.pop()
                score -= 1
            else:
                break
        
        return ans
