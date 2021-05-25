# Space     : O(n)
# Time      : O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)
        
        for i in range(n):
            if tokens[i] in ["+",  "-", "*", "/"]:
                num2, num1 = stack.pop(), stack.pop()
                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(tokens[i]))

        return stack[0]
        