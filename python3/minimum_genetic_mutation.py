from collections import defaultdict

"""
Space   : O(n^2)
Time    : O(8 * n)
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1

        change = defaultdict(list)
        bank.append(start)

        for gene in bank:
            for i in range(8):
                change[gene[:i] + '*' + gene[i+1:]].append(gene)

        visited = set()
        stack = [start]
        counter = 0
        while stack:
            temp = []
            for g in stack:
                if g in visited:
                    continue

                if g == end:
                    return counter

                for i in range(8):
                    temp += change[g[:i] + '*' + g[i+1:]]

                visited.add(g)

            temp = list(set(temp))
            stack = temp
            counter += 1

        return -1
