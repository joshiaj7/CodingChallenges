# Space : O(1)
# Time  : O(n log n)

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(0)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        mh = 0
        for i in range(1, len(horizontalCuts)):
            mh = max(mh, horizontalCuts[i] - horizontalCuts[i-1])

        mv = 0
        for j in range(1, len(verticalCuts)):
            mv = max(mv, verticalCuts[j] - verticalCuts[j-1])

        return (mh * mv) % (10**9 + 7)
