class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        """
        Personal Attempt
        Space   : O(1)
        Time    : O(n)
        """
        zs = 0

        while k - 26 >= n - 1:
            zs += 1
            k -= 26
            n -= 1

        mid = ''
        if k > n:
            mid = chr(96 + k - n + 1)
            k = k - n + 1
            n -= 1

        return 'a' * n + mid + 'z' * zs

    def getSmallestStringBest(self, n: int, k: int) -> str:
        """
        Best solution
        Math approach
        Space   : O(1)
        Time    : O(1)
        """
        # let there be x 'a', and z 'z' and maybe another alphabet 'y'

        # case 1: no need for y
        # 1.x + 26.z = k
        # x + z = n
        # x + 26(n-x) = k
        # 25x = 26n-k

        # case 2: y is needed and it can be from 2 to 25
        # 1.x + y + 26z = k
        # x + z = n - 1     or      z = n - 1 - x
        # x + y + 26(n - 1 - x) = k
        # -25x + y + 26n - 26 - k = 0
        # 25x = 26n - k - 26 + y

        if (26*n - k) % 25 == 0:  # case 1
            x = (26*n - k)//25
            ans = 'a'*x + 'z'*(n-x)
        else:   # case 2
            temp = 26*n - k - 26
            if temp < 0:
                x = 0
                y = -temp
            else:
                y = 25-(temp % 25)
                x = (temp+y)//25
            ans = 'a'*x + chr(ord('a')-1+y) + 'z'*(n-1-x)

        return ans
