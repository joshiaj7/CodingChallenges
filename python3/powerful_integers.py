# Space   : O(n)
# Time    : O(n**2)


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        p = 0
        xset = set()
        while x**p < bound:
            if x**p not in xset:
                xset.add(x**p)
            else:
                break
            p+=1
        
        p = 0
        yset = set()
        while y**p < bound:
            if y**p not in yset:
                yset.add(y**p)
            else:
                break
            p+=1
        
        ans = set()
        for a in xset:
            for b in yset:
                if a+b <= bound:
                    ans.add(a+b)
        
        return list(ans)