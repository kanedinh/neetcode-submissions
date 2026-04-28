class StockSpanner:

    def __init__(self):
        self.stack = [] # (price, span)

    def next(self, price: int) -> int:
        # res = [1] * len(self.prices)
        # stack = []

        # for i in len(self.prices):
        #     while self.stack and prices[stack[-1]] < self.prices[i]:
        #         idx = stack.pop()
        #         res[idx] = self.prices[i] + idx
        #     stack.append(i)
        # return res

        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))
        return span
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)