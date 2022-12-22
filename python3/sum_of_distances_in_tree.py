from collections import defaultdict

"""
Space   : O(n)
Time    : O(n)
"""


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        dic1 = defaultdict(list)
        for e in edges:
            dic1[e[0]].append(e[1])
            dic1[e[1]].append(e[0])
        
        exclude = {0}

        # eachItem subtreeDist[n]=[a, b] means subtree rooted at n has totally a nodes, 
        # and sum of distance in the subtree for n is b
        subtreeDist = [[0, 0] for _ in range(N)]

        ans = [0]*N
        
        def sumSubtreeDist(node, exclude):
            cnt, ret = 0, 0
            exclude.add(node)
            for x in dic1[node]:
                if x in exclude:
                    continue
                res = sumSubtreeDist(x, exclude)
                cnt += res[0]
                ret += (res[0]+res[1])
            subtreeDist[node][0] = cnt+1
            subtreeDist[node][1] = ret
            return cnt+1, ret
            
        # recursively calculate the sumDist for all subtrees 
        # 0 can be replaced with any other number in [0, N-1]
        # and the chosen root has its correct sum distance in the whole tree
        sumSubtreeDist(0, set())

        # visit and calculates the sum distance in the whole tree
        def visit(n, pre, exclude):
            if pre==-1:
                ans[n] = subtreeDist[n][1]
            else:
                ans[n] = ans[pre] - 2 * subtreeDist[n][0] + N
            exclude.add(n)
            for x in dic1[n]:
                if x not in exclude:
                    visit(x, n, exclude)
                
        visit(0, -1, set())
        return ans
