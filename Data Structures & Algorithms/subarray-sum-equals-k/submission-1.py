class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}
        curSum = 0
        count = 0

        for num in nums:
            curSum += num
            diff = curSum - k
            
            if diff in prefixSum.keys():
                count += prefixSum[diff]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return count