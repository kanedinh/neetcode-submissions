class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums.sort()
        # missing = 1

        # for num in nums:
        #     if num < 1:
        #         continue
        #     if num == missing:
        #         missing += 1
        # return missing

        hashSet = set(nums)
        missing = [_ for _ in range(1, len(nums) + 2)]

        for num in missing:
            if num not in hashSet:
                return num