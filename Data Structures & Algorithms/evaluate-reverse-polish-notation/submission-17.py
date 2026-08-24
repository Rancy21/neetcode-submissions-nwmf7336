class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens.pop())
        stack = []

        for t in tokens:
            if t =="+":
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                stack.append(num2 + num1)
            elif t == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                stack.append(num2 - num1)
            elif t == "*":
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                stack.append(num2 * num1)
            elif t == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())

                stack.append(num2 / num1)
            else:
                stack.append(t)
            
        return int(stack.pop())
        