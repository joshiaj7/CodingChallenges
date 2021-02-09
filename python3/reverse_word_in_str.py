# leetcode

class Solution:
    def reverseWords(self, s: str) -> str:
        res, words = [], []
        leng = len(s)
        
        word = ''
        for idx in range(leng):
            if s[idx] != ' ':
                word += s[idx]
            elif len(word) > 0:
                words.append(word)
                word = ''
            if idx == leng-1 and len(word) > 0:
                words.append(word)
                word = ''
        
        for i in range(len(words)-1, -1, -1):
            res.append(words[i])

        return " ".join(res)
        