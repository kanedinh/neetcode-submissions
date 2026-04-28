class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute Force
        n = len(nums)
        for num in nums:
            count = 0
            for i in nums:
                if i == num:
                    count += 1
            if count > n // 2:
                return num