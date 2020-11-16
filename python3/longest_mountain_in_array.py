class Solution:
    def insertStack(self, stack: List[int], direction: str) -> List[int]:
        if len(stack) > 0:
            if stack[-1][0] == direction:
                stack[-1][1] += 1
            else:
                stack.append([direction, 1])
        else:
            stack.append([direction, 1])

        return stack

    def longestMountain(self, A: List[int]) -> int:
        """
        Personal Attempt
        Space   : O(n)
        Time    : O(n)
        """
        ans = 0
        n = len(A)

        stack = []

        for i in range(1, n):
            if A[i] > A[i-1]:
                stack = self.insertStack(stack, "u")
            elif A[i] == A[i-1]:
                stack = self.insertStack(stack, "s")
            else:
                stack = self.insertStack(stack, "d")

        m = len(stack)
        if m == 1:
            return 0

        for j in range(m-1):
            c1, c2 = stack[j], stack[j+1]
            if c1[0] == "u" and c2[0] == "d":
                ans = max(ans, c1[1] + c2[1] + 1)

        return ans

    def longestMountain2(self, A: List[int]) -> int:
        """
        Best Solution
        Space   : O(1)
        Time    : O(n)
        """
        lastup = lastdown = ans = was = 0
        for i in range(1, len(A)):
            if A[i]-A[i-1] > 0:
                lastdown = 0
                lastup += 1
            elif A[i]-A[i-1] < 0:
                if lastup > 0:
                    was = lastup + 1
                lastup = 0
                lastdown += 1
                if was > 0:
                    ans = max(ans, was+lastdown)
            else:
                lastdown = 0
                lastup = 0
                was = 0
        return ans
