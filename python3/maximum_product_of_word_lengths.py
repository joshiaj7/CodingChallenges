# Space : O(n)
# Time  : O(n**2)

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def checkContainedKey(a, b):
            for k in a.keys():
                if k in b:
                    return True
            
            return False
        
        ans = 0
        word_dicts = []
        
        for word in words:
            d = {}
            m = len(word)
            for letter in word:
                d[letter] = 1
            word_dicts.append(d)    
            
        n = len(word_dicts)
        
        for i in range(n):
            for j in range(i+1, n):
                if not checkContainedKey(word_dicts[i], word_dicts[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans
        
        
        