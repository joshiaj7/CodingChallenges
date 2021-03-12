# space : O(1)
# time  : O(n)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        checklist = set()
        n = len(s)
        
        for i in range(n-k+1):
            checklist.add(s[i:i+k])
        
        return len(checklist) == 2 ** k
