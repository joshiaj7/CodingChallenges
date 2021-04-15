"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def fib(self, n: int) -> int:
        mem = [0, 1]
        if n <= 1:
            return mem[n]

        for i in range(2, n+1):
            mem.append(mem[i-1] + mem[i-2])

        return mem[-1]
