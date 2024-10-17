from heapq import heappush, heappop

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        
        h = []
        if a > 0:
            heappush(h, (-a, "a"))
        if b > 0:
            heappush(h, (-b, "b"))
        if c > 0:
            heappush(h, (-c, "c"))

        while h:
            count1, c1 = heappop(h)

            if len(ans) >= 2 and ans[-1] == c1 and ans[-2] == c1:
                if not h:
                    break

                count2, c2 = heappop(h)
                ans += c2
                count2 += 1

                if count2 < 0:
                    heappush(h, (count2, c2))

                heappush(h, (count1, c1))
            else:
                ans += c1
                count1 += 1

                if count1 < 0:
                    heappush(h, (count1, c1))

        return ans
