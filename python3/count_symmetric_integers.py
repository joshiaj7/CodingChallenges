class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0

        for i in range(low, high+1):
            s = str(i)
            leng = len(s)

            if len(s) % 2 == 1:
                continue

            firstHalf = s[:leng//2]
            secondHalf = s[leng//2:]
            
            sumFirst = 0
            for j in firstHalf:
                sumFirst += int(j)

            sumSecond = 0
            for j in secondHalf:
                sumSecond += int(j)   

            if sumFirst == sumSecond:
                ans += 1
            
        return ans
