# Space : O(len(word))
# Time  : O(n * len(word))

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        pn = len(pattern)

        for word in words:
            if len(word) != pn:
                continue

            mem1, mem2 = {}, {}
            defect = False
            for i in range(pn):
                if word[i] not in mem1:
                    mem1[word[i]] = pattern[i]
                elif mem1[word[i]] != pattern[i]:
                    defect = True
                    break

                if pattern[i] not in mem2:
                    mem2[pattern[i]] = word[i]
                elif mem2[pattern[i]] != word[i]:
                    defect = True
                    break

            if defect:
                continue

            if len(mem1) == len(mem2):
                ans.append(word)

        return ans
