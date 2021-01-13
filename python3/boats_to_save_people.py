class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Beats 10%
        Time    : O(n)
        Space   : O(n)
        """
        ans = 0
        n = len(people)
        d = {}
        max_w, min_w = 0, 30000

        for x in people:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
            max_w = max(max_w, x)
            min_w = min(min_w, x)

        for i in range(min_w, max_w):
            if i not in d:
                d[i] = 0

        s, e = min_w, max_w

        while s < e:
            if s + e > limit:
                ans += d[e]
                d[e] = 0
                e -= 1
            else:
                if d[s] == 0:
                    s += 1
                    continue
                if d[e] == 0:
                    e -= 1
                    continue
                slices = min(d[s], d[e])
                ans += slices
                d[s] -= slices
                d[e] -= slices
                if d[s] == 0:
                    s += 1
                if d[e] == 0:
                    e -= 1

        if d[s] > 0:
            if 2 * s <= limit:
                ans += d[s] // 2
                ans += d[s] % 2
            else:
                ans += d[s]

        return ans

    def numRescueBoatsBest(self, people: List[int], limit: int) -> int:
        """
        Beats 30%
        Time    : O(n log n)
        Space   : O(1)
        """
        ans = 0
        people.sort()
        s, e = 0, len(people)-1

        while s <= e:
            if people[s] + people[e] <= limit:
                s += 1
            e -= 1
            ans += 1

        return ans
