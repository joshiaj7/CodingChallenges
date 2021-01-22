from collections import Counter


class Solution:
    def closeStringsCounter(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        if c1.keys() != c2.keys():
            return False

        if Counter(c1.values()) != Counter(c2.values()):
            return False

        return True

    def closeStringsGeneric(self, word1: str, word2: str) -> bool:
        n = len(word1)
        m = len(word2)

        if n != m:
            return False

        d1, d2 = {}, {}
        count1, count2 = {}, {}

        for i in range(n):
            if word1[i] not in d1:
                d1[word1[i]] = 1
            else:
                d1[word1[i]] += 1

            if word2[i] not in d2:
                d2[word2[i]] = 1
            else:
                d2[word2[i]] += 1

        # len check
        if len(d1) != len(d2):
            return False

        # key check
        for k, _ in d1.items():
            if k not in d2:
                return False

        for _, v in d1.items():
            if v not in count1:
                count1[v] = 1
            else:
                count1[v] += 1

        for _, v in d2.items():
            if v not in count2:
                count2[v] = 1
            else:
                count2[v] += 1

        for key, val in count1.items():
            if key not in count2:
                return False
            if count2[key] != val:
                return False

        return True
