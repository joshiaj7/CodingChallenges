"""
Space : O(len(word))
Time  : O(n * len(word))
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        for word in words:
            mem_w = {}
            mem_p = {}
            safe = True
            for i in range(len(word)):
                w = word[i]
                p = pattern[i]
                
                if w not in mem_w and p not in mem_p:
                    mem_w[w] = p
                    mem_p[p] = w
                elif w in mem_w and p in mem_p and mem_w[w] == p and mem_p[p] == w:
                    continue
                else:
                    safe = False
                    break
        
            if not safe:
                continue

            ans.append(word)
        
        
        return ans
