class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        countMap = Counter(nums)
        return any(v > 1 for v in countMap.values())