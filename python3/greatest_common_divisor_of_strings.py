from math import gcd

"""
Space   : O(n1 + n2)
Time    : O(n1^2 + n2^2)
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        n1, n2 = len(str1), len(str2)
        d1, d2 = {}, {}

        for i in range(n1):
            if n1 % (i+1) == 0 and str1[:i+1] * (n1 // (i+1)) == str1:
                d1[str1[:i+1]] = 1
                
        for i in range(n2):
            if n2 % (i+1) == 0 and str2[:i+1] * (n2 // (i+1)) == str2:
                d2[str2[:i+1]] = 1

        for k in d1.keys():
            if k in d2 and len(k) > len(ans):
                ans = k

        return ans

    def gcdOfStringsSimple(self, str1: str, str2: str) -> str:
    # we can approach this mathematically
    # if two numbers have a common divisor, this means that two numbers can be expressed as a multiple of that divisor
    # so looking at the below example
    # a = 4, b = 6..we see that ab (4 * 6)->[2*2*2*2*2] = ba (6 * 4)->[2*2*2*2*2]
    # Therefore two strings would have a common divisor if the concantentation of the two strings are equal in both ways
    # stringa + stringb = stringb + stringa
    # Once we know this, we just need to find the gcd of the two strings lenght and return the string up to that length
        if str1 + str2 != str2 + str1:
            return ""
        gcdLength = gcd(len(str1), len(str2))
        return str1[:gcdLength]
