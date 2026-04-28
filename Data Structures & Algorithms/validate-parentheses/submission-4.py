class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}":"{","]":"["}
        for c in s:
            # if stack:
            #     if stack[-1] == "(" and c == ")":
            #         stack.pop()
            #     elif stack[-1] == "{" and c == "}":
            #         stack.pop()
            #     elif stack[-1] == "[" and c == "]":
            #         stack.pop()
            #     else:
            #         stack.append(c)
            # else:
            #     stack.append(c)
            if stack and c in pairs and stack[-1] == pairs[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack