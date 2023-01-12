from collections import defaultdict, Counter

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        graph = defaultdict(list)

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        def dfs(node, prev, labels):
            count = Counter()
            for neighbor in graph[node]:
                if neighbor != prev:
                    count += (dfs(neighbor, node, labels))

            count[labels[node]] += 1
            ans[node] = count[labels[node]]

            return count


        dfs(0, -1, labels)
        return ans
