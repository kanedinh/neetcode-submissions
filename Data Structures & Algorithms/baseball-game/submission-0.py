class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for s in operations:
            if s == "+":
                stack.append(stack[-1] + stack[-2])
            elif s == "D":
                stack.append(stack[-1] * 2)
            elif s == "C":
                stack.pop()
            else:
                stack.append(int(s))
        
        # total = 0
        # for num in stack:
        #     total += num
        # return total
        return sum(stack)
