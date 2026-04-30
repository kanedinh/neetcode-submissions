class Solution:
    def tribonacci(self, n: int) -> int:
        # DP Bottom-Up
        # if n <= 2:
        #     return 1 if n != 0 else 0

        # T = [0] * (n + 1)
        # T[1] = T[2] = 1
        # for i in range(3, n+1):
        #     T[i] = T[i - 3] + T[i - 2] + T[i - 1]
        # return T[n]

        # DP Top-Down
        T = [-1] * (n+1)
        def dfs(i):
            if i <= 2:
                return 1 if i != 0 else 0
            if T[i] != -1:
                return T[i]
            T[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return T[i]
        return dfs(n)
                