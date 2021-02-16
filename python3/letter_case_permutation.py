"""
Space   : O(n**2)
Time    : O(n**2)
where n = number of letters in S
"""


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permute(S, path):
            if len(S) == 0:
                ans.append(path)
                return
            if S[0].isalpha():
                permute(S[1:], path + S[0].upper())
                permute(S[1:], path + S[0].lower())
            else:
                permute(S[1:], path + S[0])

        ans = []
        permute(S, '')

        return ans
