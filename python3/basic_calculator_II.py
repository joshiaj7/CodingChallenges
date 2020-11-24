class Solution:
    def calculate(self, s: str) -> int:
        """
        Personal Attempt
        Space   : O(n)
        Time    : O(n)
        """
        if len(s) == 0:
            return 0

        stack = []
        for i in s:
            if i == ' ':
                continue
            elif i.isdigit():
                if not stack or not stack[-1][0].isdigit():
                    stack.append(i)
                else:
                    stack[-1] += i
            else:
                stack.append(i)

        if len(stack) == 1:
            return int(stack[0])

        # eliminate * and / first
        j = 1
        while j < len(stack) and len(stack) > 2:
            if stack[j] in ["*", "/"]:
                a = int(stack.pop(j-1))
                op = stack.pop(j-1)
                b = int(stack.pop(j-1))
                if op == "*":
                    stack.insert(j-1, a * b)
                else:
                    stack.insert(j-1, a // b)
            else:
                j += 2

        ans = int(stack[0])
        for k in range(1, len(stack), 2):
            if stack[k] == '+':
                ans += int(stack[k+1])
            else:
                ans -= int(stack[k+1])

        return ans

    def calculateBest(self, s):
        """
        :type s: str
        :rtype: int
        Best Solution
        Space   : O(n)
        Time    : O(n)
        """

        stack = []
        num = 0
        presig = '+'
        s = s+'+'

        for i in s:
            if i.isdigit():
                num = num*10+int(i)
            elif i != ' ':
                if presig == '+':
                    stack.append(num)
                elif presig == '-':
                    stack.append(-num)
                elif presig == '*':
                    stack[-1] = stack[-1]*num
                elif presig == '/':
                    stack[-1] = int(float(stack[-1])/num)
                num = 0
                presig = i
        return sum(stack)
