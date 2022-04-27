from collections import defaultdict

# Space : O(n)
# Time  : O(n^2)

# Method:
# Disjoint Set (Or Union-Find)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])
            return parent[x]

        def union(x, y):
            parent[find_parent(x)] = find_parent(y)

        l = len(s)
        parent = [i for i in range(l)]

        # unionize : fill parent list with reference for each index
        for x, y in pairs:
            union(x, y)

        # fill graph with joint unionize indices
        graph = defaultdict(list)
        for i in range(l):
            graph[find_parent(i)].append(i)

        # build the word
        res = [''] * l
        for x in graph:
            temp = []
            for y in graph[x]:
                temp.append(s[y])
            temp.sort()
            graph[x].sort()
            for i, v in enumerate(graph[x]):
                res[v] = temp[i]

        return "".join(res)
