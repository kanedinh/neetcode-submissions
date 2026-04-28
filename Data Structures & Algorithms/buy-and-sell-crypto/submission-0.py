class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return profit

        # profit = 0
        # min_price = prices[0]

        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = max(profit, price - min_price)
        # return profit