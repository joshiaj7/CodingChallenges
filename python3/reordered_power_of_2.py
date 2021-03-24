# Space : O(n)
# Time	: O(log n)


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        power = 0
        leng = len(str(N))
        n_map = {}
        
        for l in str(N):
            if l not in n_map:
                n_map[l] = 1
            else:
                n_map[l] += 1
        
        cmp = 1
        while len(str(cmp)) <= leng:
            if len(str(cmp)) == leng:
                cmp_map = {}
                for m in str(cmp):
                    if m not in cmp_map:
                        cmp_map[m] = 1
                    else:
                        cmp_map[m] += 1
                if cmp_map == n_map:
                    return True
            power += 1
            cmp = 2 ** power
        
        
        return False
