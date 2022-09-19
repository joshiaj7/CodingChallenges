"""
Space   : O(n)
Time    : O(n * m * m)
"""


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        n = len(words)
        d = {}
        for i, w in enumerate(words):
            d[w] = i

        ans = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in d:
                        ans.append([d[back], i])
                if j != m and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in d:
                        ans.append([i, d[back]])

        return ans
