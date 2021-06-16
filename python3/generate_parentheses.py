# Space : O(n)
# Time  : O(n**3)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        ans = {"()"}
        for i in range(n-1):
            temp = set()
            for item in ans:
                for j in range(len(item)):
                    temp.add(item[:j] + "()" + item[j:])
            ans = temp

        return ans
