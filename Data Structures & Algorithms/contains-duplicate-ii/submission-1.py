class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # mp = {}

        # for i in range(len(nums)):
        #     if nums[i] in mp and i - mp[nums[i]] <= k:
        #         return True
        #     mp[nums[i]] = i

        # return False

        hashSet = set()

        l, r = 0, 0

        while r < len(nums):
            if r - l > k:
                hashSet.remove(nums[l])
                l += 1
            if nums[r] in hashSet:
                return True
            hashSet.add(nums[r])
            r += 1
        return False