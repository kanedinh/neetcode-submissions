class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if stack:
                if stack[-1] == "(" and c == ")":
                    stack.pop()
                elif stack[-1] == "{" and c == "}":
                    stack.pop()
                elif stack[-1] == "[" and c == "]":
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return not stack