from typing import List

"""
Space   : O(right)
Time    : O(right)
Sieve of Eratosthenes
"""

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:        
        isPrime = [True for i in range(right+1)]
        isPrime[0] = False
        isPrime[1] = False
        ans = [-1, -1]

        i = 2
        while i*i <= right:
            if not isPrime[i]:
                i += 1
                continue

            j = i*i
            while j <= right:
                isPrime[j] = False
                j += i
            i += 1

        diff = float('inf')
        i = 0
        j = left
        while left <= j <= right:
            if isPrime[j]:
                if i == 0:
                    i = j
                    j += 1
                    continue

                if j - i < diff:
                    diff = j - i
                    ans = [i, j]
                
                i = j

            j += 1

        return ans
