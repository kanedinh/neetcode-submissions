class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Mem: O(n)
        res = [0] * len(nums)
        for i in range(len(nums)):
            j = (i + k) % len(nums)
            res[j] = nums[i]
        nums[:] = res