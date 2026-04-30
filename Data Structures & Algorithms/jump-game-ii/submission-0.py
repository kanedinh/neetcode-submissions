class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        res = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1        
        return res
        # 2 1 2 1 0
        # lr
        #   l r
        #       l r
        # max(0, 1 + 1, 2 + 2) = 4