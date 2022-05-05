# Space     : O(n^2)
# Time      : O(n!)

# string permutation here

def stringPermutation(s):
    def permute(s, w):
        if len(s) == 0:
            ans.append(w)
        for i in range(len(s)):
            permute(s[:i] + s[i+1:], w + s[i])

    ans = []
    permute(s, "")
    print(ans)


stringPermutation("1234")
