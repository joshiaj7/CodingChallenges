# Space   : O(1)
# Time    : O(n)

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        s, e = 2, n
        ans = [1]
        
        while s <= e:
            if k > 1:
                if ans[-1] == s-1:
                    ans.append(e)
                    e -= 1
                elif ans[-1] == e+1:
                    ans.append(s)
                    s += 1
                k -= 1
            else:
                if ans[-1] == s-1:
                    ans.append(s)
                    s += 1
                elif ans[-1] == e+1:
                    ans.append(e)
                    e -= 1
        
        return ans
        