class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s, hash_t = {}, {}

        for i in range(len(t)):
            if i != len(s):
                if s[i] not in hash_s:
                    hash_s[s[i]] = 1
                else:
                    hash_s[s[i]] += 1
            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1
                
        for k, v in hash_t.items():
            if k in hash_s:
                if abs(v - hash_s[k]) == 1:
                    return k
            else:
                return k
        