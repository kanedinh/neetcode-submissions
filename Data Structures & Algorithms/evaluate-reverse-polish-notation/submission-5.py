class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if stack:
                if c == "+":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a+b)
                elif c == "-":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a-b)
                elif c == "*":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a*b)
                elif c == "/":
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a/b))
                else:
                    stack.append(int(c))
            else:
                stack.append(int(c))
        return int(stack[0])