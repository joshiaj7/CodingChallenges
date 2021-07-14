# Space : O(n)
# Time  : O(n log n)

class Solution:
    def customSortString(self, order: str, string: str) -> str:
        d = {l: i for i, l in enumerate(order)}
        res = sorted(string, key=lambda l: d[l] if l in d else -1)

        return "".join(res)
