"""
Space   : O(n)
Time    : O(nm)

Method:
Greedy
make target from "ababc" -> "?????"
"""


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """

        """
        t = len(target)  # n
        s = len(stamp)  # m
        lt = list(target)
        ls = list(stamp)
        ans = []

        def check(i):
            changed = False
            for j in range(s):
                if lt[i + j] == '?':
                    continue
                if lt[i + j] != ls[j]:
                    return False
                changed = True
            if changed:
                ans.append(i)
                for j in range(s):
                    lt[i + j] = '?'
            return changed

        changed = True
        while changed:
            changed = False
            for i in range(t - s + 1):
                changed |= check(i)
                if changed:
                    break

        return ans[::-1] if lt == ['?'] * t else []
