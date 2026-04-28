class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        s = 0
        mini = len(nums) + 1
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                mini = min(mini, r - l + 1)
                s -= nums[l]
                l += 1
        
        return 0 if mini == len(nums) + 1 else mini