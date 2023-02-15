"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        ks = str(k)
        lk, ln = len(ks), len(num)
        n = max(lk, ln)

        for i in range(n - lk):
            ks = "0" + ks

        for i in range(n - ln):
            num = [0] + num

        rem = 0
        for i in range(n-1, -1, -1):
            v = int(ks[i])

            count = v + num[i] + rem
            num[i] = count % 10
            rem = count // 10

        if rem > 0:
            num = [rem] + num

        return num
