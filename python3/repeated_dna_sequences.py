"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        hashmap = {}
        n = len(s)

        if n < 10:
            return []

        for i in range(n-9):
            if s[i:i+10] not in hashmap:
                hashmap[s[i:i+10]] = 1
            else:
                hashmap[s[i:i+10]] += 1

        for k, v in hashmap.items():
            if v > 1:
                ans.append(k)

        return ans
