class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        for num in nums:
            if num < 1:
                continue
            if num == missing:
                missing += 1
        return missing