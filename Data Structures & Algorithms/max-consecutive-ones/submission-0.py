class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 0
        leng = 0
        for num in nums:
            if num == 1:
                leng += 1
                maxLength = max(leng, maxLength)
            else:
                leng = 0
        return maxLength