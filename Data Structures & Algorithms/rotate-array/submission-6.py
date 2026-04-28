class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Mem: O(n)
        # res = [0] * len(nums)
        # for i in range(len(nums)):
        #     j = (i + k) % len(nums)
        #     res[j] = nums[i]
        # nums[:] = res

        # Mem: O(1)
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k %= n

        reverse(nums, 0, n - 1) # Step 1: reverse the array
        reverse(nums, 0, k - 1) # Step 2: reverse the subarray from 0 -> k - 1
        reverse(nums, k, n - 1) # Step 3: reverse the subarray from k -> n - 1