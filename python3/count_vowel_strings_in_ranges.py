from typing import List

"""
Space   : O(n)
Time    : O(n)
"""

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        pref = [0]
        vowels = {
            'a': True,
            'e': True,
            'i': True,
            'o': True,
            'u': True,
        }

        for s in words:
            count = 0
            if s[0] in vowels and s[-1] in vowels:
                count = 1

            pref.append(pref[-1] + count)
            
        for s, e in queries:
            left = pref[s]
            right = pref[e+1]

            ans.append(right - left)



        return ans
        