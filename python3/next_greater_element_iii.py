from itertools import permutations


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        Personal attempt
        Space   : O(n)
        Time    : O(n!)
        """

        if n < 10:
            return -1

        a = list(str(n))

        ans = -1
        perms = permutations(a)

        for i in list(perms):
            num = int("".join(i))

            if num > n and num < 2 ** 31:
                if ans == -1:
                    ans = num
                else:
                    ans = min(ans, num)

        return ans

    def nextGreaterElementBest(self, n: int) -> int:
        """
        Best Solution
        Space   : O(n)
        Time    : O(n)
        """
        s = list(str(n))
        l = len(s)
        i = l-1

        for i in range(i, -1, -1):
            if s[i-1] < s[i]:
                i -= 1
                break
            i -= 1

        if i < 0:
            return -1

        for j in range(l-1, i, -1):
            if s[j] > s[i]:
                s[j], s[i] = s[i], s[j]
                break

        s[i+1:] = s[i+1:][::-1]
        val = int(''.join(s))
        return val if val < (2**31)-1 else -1
