# Space : O(n)
# Time  : O(n)

class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        if not shifts:
            return S
        
        n = len(shifts)
        con = [0] * n
        
        for i in range(n-1, -1, -1):
            if i == n-1:
                con[i] = shifts[i] % 26
            else:
                con[i] = (shifts[i] + con[i+1]) % 26

        ans = ''
        for j in range(n):
            ans += chr(97 + ((ord(S[j]) - 97 + con[j]) % 26))

        return ans