# Space : O(n)
# Time  : O(n log n)

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n, h = len(arr), len(arr)//2
        d = {}

        for x in arr:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        s = sorted(d.items(), key=lambda item: item[1], reverse=True)

        ans = 0
        for _, freq in s:
            if n > h:
                n -= freq
                ans += 1

        return ans
