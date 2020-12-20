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
                return S[j]

            if S[j].isdigit():
                size //= int(S[j])
            else:
                size -= 1

        return S[K]
