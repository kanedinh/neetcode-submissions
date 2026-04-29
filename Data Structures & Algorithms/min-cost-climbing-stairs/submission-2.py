class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # DFS recursive
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     return cost[i] + min(dfs(i + 1), dfs(i + 2))
        # return min(dfs(0),dfs(1))

        # DP Top-Down
        # cache = [-1] * len(cost)

        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        #     return cache[i]
        # return min(dfs(0), dfs(1))

        # DP Bottom-Up
        n = len(cost)
        cache = [0] * (n + 1)
        for i in range(2, n + 1):
            cache[i] = min(cache[i - 1] + cost[i - 1], cache[i - 2] + cost[i - 2])
        return cache[n]