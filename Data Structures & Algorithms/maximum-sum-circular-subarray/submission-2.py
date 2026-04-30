class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMin = min(curMin + num, num)
            curMax = max(curMax + num, num)
            total += num
            globMin = min(globMin, curMin)
            globMax = max(globMax, curMax)
        return max(globMax, total - globMin)