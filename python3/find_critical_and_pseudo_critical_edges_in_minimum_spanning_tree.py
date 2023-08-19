import collections
from typing import List

class UnionFindSet:
    def __init__(self, n=0):
        self.parents = {}
        self.ranks = {}
        self.count = 0
        for i in range(n):
            self.add(i)

    def add(self, p):
        self.parents[p] = p
        self.ranks[p] = 1
        self.count += 1

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: 
            return False
        if self.ranks[pu] < self.ranks[pv]:
            self.parents[pu] = pv
        elif self.ranks[pu] > self.ranks[pv]:
            self.parents[pv] = pu
        else:        
            self.parents[pv] = pu
            self.ranks[pu] += 1
        self.count -= 1
        return True


"""
Space   : O(E)
Time    : O(E log E)
"""

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    
        # reference: LC 1192
        def dfs(curr, level, parent):
            levels[curr] = level
            for child, i in graph[curr]:
                if child == parent:
                    continue
                elif levels[child] == -1:
                    levels[curr] = min(levels[curr], dfs(child, level + 1, curr))
                else:
                    levels[curr] = min(levels[curr], levels[child])
                if levels[child] >= level + 1 and i not in p_cri:
                    cri.add(i)
            return levels[curr]
        
        # init critical and pseudo-critical edge set
        cri, p_cri = set(), set()
        
        # use dic to store all edges associated with a given weight
        dic = collections.defaultdict(list)
        for i, (u, v, w) in enumerate(edges):
            dic[w].append([u, v, i])
        
        # define union find et
        union_set = UnionFindSet(n)
        
        # iterate through all weights in ascending order
        for w in sorted(dic):
                
            # seen[(pu, pv)] contains all edges connecting pu and pv,
            # where pu and pv are the parent nodes of their corresponding groups
            seen = collections.defaultdict(set)
            # populate seen
            for u, v, i in dic[w]:
                pu, pv = union_set.find(u), union_set.find(v)
                # skip the edge that creates cycle
                if pu == pv:
                    continue
                seen[min(pu, pv), max(pu, pv)].add(i) # edge i connects pu and pv
            
            # w_edges contains all weight-w edges we may add to MST
            w_edges, graph = [], collections.defaultdict(list)
            for pu, pv in seen:
                # more than 1 edge can connect pu and pv
                # these edges are pseudo-critical
                if len(seen[pu, pv]) > 1:
                    p_cri |= seen[pu, pv]
                # construct graph for weight w 
                edge_idx = seen[pu, pv].pop()
                graph[pu].append((pv, edge_idx))
                graph[pv].append((pu, edge_idx))
                w_edges.append((pu, pv, edge_idx))
                # union pu and pv groups
                union_set.union(pu, pv)
            
            # run dfs to mark all critical w_edges
            levels = [-1] * n
            for u, v, i in w_edges:
                if levels[u] == -1:
                    dfs(u, 0, -1)
            # the edges in w_edges cycles are pseudo-critical
            for u, v, i in w_edges:
                if i not in cri:
                    p_cri.add(i)
        
        return [cri, p_cri]
