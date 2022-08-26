from collections import Counter

"""
Space   : O(len(n))
Time    : O(log n)
"""


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sn = str(n)
        n_len = len(sn)
        cn = Counter(sn)
        
        count = 1
        while True:
            s_count = str(count)
            if len(s_count) > n_len:
                break
            if len(s_count) == n_len:
                cc = Counter(s_count)
                if len(cc - cn) == 0:
                    return True
                
            count <<= 1
        
        return False
