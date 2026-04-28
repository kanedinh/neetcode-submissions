class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1, n + 1)]

        def dfs(i, subset):
            if len(subset) == k:
                res.append(subset.copy())
                return
            if i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)
        dfs(0, [])

        return res