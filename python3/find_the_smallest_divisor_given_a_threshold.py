class Solution:
    def getTotal(self, nums: List[int], m: int) -> int:
        total = 0
        for i in nums:
            div = i // m
            remain = i % m

            if remain >= 1:
                div += 1

            total += div

        return total

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s, e = 1, max(nums)
        mem = {}

        while s <= e:
            m = (s + e) // 2
            total = self.getTotal(nums, m)

            mem[m] = total
            if total < threshold:
                if (m-1) in mem:
                    if mem[m-1] > threshold:
                        return m
                else:
                    e = m - 1
            elif total == threshold:
                break
            elif total > threshold:
                if (m+1) in mem:
                    if mem[m+1] < threshold:
                        return m+1
                else:
                    s = m + 1

        while total == threshold and m > 1:
            new_total = self.getTotal(nums, m-1)
            if new_total == total:
                m -= 1
            else:
                return m

        return 1

    # best solution
    def smallestDivisor2(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            m = (l + r) // 2
            if sum((i + m - 1) // m for i in nums) > threshold:
                l = m + 1
            else:
                r = m
        return l
