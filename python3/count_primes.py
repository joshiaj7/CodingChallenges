# Space   : O(n)
# Time    : O(n log n)


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        i = 2
        while i*i < n:
            if not isPrime:
                continue
            j = i*i
            while j < n:
                isPrime[j] = False
                j += i
            i += 1

        count = 0
        for x in isPrime:
            if x:
                count += 1
            
        return count