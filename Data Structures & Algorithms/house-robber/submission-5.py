class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP Top-Down
        # n = len(nums)
        # dp = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
        #     return dp[i]
        # return dfs(0)
        # [1, 2, 3, 1]
        # [1, 2, 4, 4]
        # DP Bottom-Up
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, n):
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        # return dp[n - 1]
        
        # [a, b, n, n+1, ...]
        a, b = 0, 0
        for n in nums:
            tmp = max(a + n, b)
            a = b
            b = tmp
        return b