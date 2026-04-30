class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # # backtracking
        # def dfs(i):
        #     if i == len(s):
        #         return True

        #     for w in wordDict:
        #         if ((i + len(w)) <= len(s) and
        #              s[i : i + len(w)] == w
        #         ):
        #             if dfs(i + len(w)):
        #                 return True
        #     return False

        # return dfs(0)

        # DP Top-Down
        # wordDict = set(wordDict)
        # dp = {len(s) : True}

        # def dfs(i):
        #     if i == len(s):
        #         return True
        #     if i in dp:
        #         return dp[i]
        #     for w in wordDict:
        #         if ((i + len(w)) <= len(s) and
        #              s[i : i + len(w)] == w
        #         ):
        #             if dfs(i + len(w)):
        #                 dp[i] = True
        #                 return True
        #     dp[i] = False
        #     return False
        # return dfs(0)

        # DP Bottom-Up
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s) and s[i: i + len(w)] == w):
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]