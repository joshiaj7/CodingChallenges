import heapq

"""
Space   : O(n)
Time    : O(n log n)
"""

class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}

        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1

        heap = [(-v, k) for k, v in hashmap.items()]
        heapq.heapify(heap)
        
        new_s = []
        prev_val, prev_key = 0, ""
        while heap:
            val, key = heapq.heappop(heap)
            new_s.append(key)
            if prev_val < 0:
                heapq.heappush(heap, (prev_val, prev_key))
            val += 1
            prev_val, prev_key = val, key

        ans = ''.join(new_s)
        return "" if len(ans) != len(s) else ans
