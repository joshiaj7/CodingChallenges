"""
Space   : O(n)
Time    : O(n * 2 ^ leng)
"""


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        d = set(words)

        def dfs(word):
            for i in range(len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    return True
                if prefix in d and dfs(suffix):
                    return True
                if suffix in d and dfs(prefix):
                    return True

            return False

        for word in words:
            if dfs(word):
                ans.append(word)

        return ans
