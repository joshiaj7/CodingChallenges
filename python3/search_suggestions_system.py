from collections import defaultdict

"""
Space   : O(n**2)
Time    : O(n**2)

Method:
prefix transversal
"""


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products.sort()

        pref = defaultdict(list)
        for word in products:
            for i in range(1, len(word)+1):
                p = word[:i]
                if p in pref and len(pref[p]) == 3:
                    continue
                pref[p].append(word)

        for i in range(1, len(searchWord)+1):
            ans.append(pref[searchWord[:i]])

        return ans
