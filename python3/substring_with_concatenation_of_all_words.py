"""
Space   : O(n)
Time    : O(nk)
"""


class Solution:
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []

        n = len(words[0])
        d = {}

        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        i = 0
        ans = []

        # sliding window(s)
        for k in range(n):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-n+1, n):
                tword = s[j:j+n]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + n
                    subd = {}
                    count = 0

        return ans
