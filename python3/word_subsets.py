from collections import Counter
from typing import List

"""
Space   : O(n)
Time    : O(n + m)
"""

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count = Counter()
        for w in words2:
            count |= Counter(w)

        ans = []
        for w in words1:
            if not (count - Counter(w)):
                ans.append(w)
        return ans

    def wordSubsets2(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = []
        allC = {}

        for w in words2:
            temp = {}
            for l in w:
                if l in temp:
                    temp[l] +=1
                else:
                    temp[l] = 1

            for k, v in temp.items():
                if k not in allC:
                    allC[k] = v
                else:
                    allC[k] = max(allC[k], v) 

        for w in words1:
            isUniv = True

            temp = {}
            for l in w:
                if l in temp:
                    temp[l] +=1
                else:
                    temp[l] = 1

            for k, v in allC.items():
                if k not in temp:
                    isUniv = False
                    break

                if temp[k] < v:
                    isUniv = False
                    break

            if isUniv:
                ans.append(w)

        return ans
        