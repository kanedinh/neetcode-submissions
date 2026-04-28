class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack = []
        # cur = ""

        # for c in path + "/":
        #     if c == "/":
        #         if cur == "..":
        #             if stack: stack.pop()
        #         elif cur != "" and cur != ".":
        #             stack.append(cur)
        #         cur = ""
        #     else:
        #         cur += c
        # return "/" + "/".join(stack)

        stack = []
        names = [el for el in path.split('/') if el]
        for name in names:
            if name == "..":
                if stack: stack.pop()
            elif name != ".":
                stack.append(name)
        return "/" + "/".join(stack)