class Solution:
    def numSquares(self, n: int) -> int:
        # DP Bottom-Up
        dp = [n] * (n + 1)
        dp[0] = 0

        for t in range(1, n + 1):
            for s in range(1, t + 1):
                square = s * s
                if t - square < 0:
                    break
                dp[t] = min(dp[t], dp[t - square] + 1)
        return dp[n]