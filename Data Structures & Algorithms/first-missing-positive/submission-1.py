class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Brute Force
        missing = 1

        for i in range(len(nums)):
            if missing in nums:
                missing += 1
            else:
                return missing
        return missing