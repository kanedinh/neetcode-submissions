class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)

        i, j = 0, 0
        while j < k:
            nums[i] = nums[j]
            while j < k and nums[i] == nums[j]:
                j += 1
            i += 1
        return i            