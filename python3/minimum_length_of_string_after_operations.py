class Solution:
    def minimumLength(self, s: str) -> int:
        ans = 0
        d = {}

        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        for _, v in d.items():
            v %= 2
            if v == 0:
                v = 2
            ans += v

        return ans
        