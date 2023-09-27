"""
Space   : O(1)
Time    : O(n)
"""


class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        n = len(S)

        for i in range(n):
            if S[i].isdigit():
                size *= int(S[i])
            else:
                size += 1

        for j in range(n-1, -1, -1):
            K %= size

            if K == 0 and not S[j].isdigit():
                if K == 0:
                    return S[j]
                
                size -= 1
            else:
                size //= int(S[j])

        return S[K]
