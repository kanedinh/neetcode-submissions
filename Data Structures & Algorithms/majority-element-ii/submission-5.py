from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute Force -> Time: O(n^2), Mem: O(1)
        # res = []

        # for num in nums:
        #     count = 0
        #     for i in nums:
        #         if num == i:
        #             count += 1
        #     if count > len(nums) // 3 and num not in res:
        #         res.append(num)
        # return res

        # Counter
        res = set()
        count = Counter(nums)
        for key in nums:
            if count[key] > len(nums) // 3:
                res.add(key)
        return list(res)

        