"""
Space   : O(1)
Time    : O(n)
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        primes = [2, 3, 5]
        next_ugly = [2, 3, 5]
        increase = [1, 1, 1]
        arr = [1]

        for i in range(1, n):
            smallest = min(next_ugly)
            arr.append(smallest)

            for i in range(3):
                if next_ugly[i] == smallest:
                    increase[i] += 1
                    next_ugly[i] = primes[i] * arr[increase[i] - 1] 

        return arr[-1]