"""
Space   : O(n)
Time    : O(n log n)
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        score = 0
        n = len(tokens)
        dp = [0] * n

        tokens = sorted(tokens)

        s, e = 0, len(tokens)-1
        while s <= e:
            if P - tokens[s] >= 0:
                P -= tokens[s]
                dp[s] += 1
                s += 1
                score += 1
            else:
                if score > 0:
                    cost = 0
                    while P < tokens[s]:
                        P += tokens[e]
                        score -= 1
                        cost += 1
                        e -= 1
                        if score == 0:
                            break
                    dp[s] -= cost
                else:
                    break

        ans = 0
        count = 0
        for i in dp:
            count += i
            ans = max(ans, count)

        return ans
