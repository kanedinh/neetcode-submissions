class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0: 
        #     return 0

        # nums.sort()

        # longest = 1
        # curr = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         continue
        #     elif nums[i] == nums[i - 1] + 1:
        #         curr += 1
        #     else:
        #         longest = max(curr, longest)
        #         curr = 1
        
        # return max(longest, curr)

        numSet = set(nums)
        longest = 0

        for num in numSet:
            length = 1
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
            longest = max(longest, length)
        return longest
