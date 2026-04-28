from collections import Counter, defaultdict
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

        # # Counter -> Time & Mem: O(n)
        # res = set()
        # count = Counter(nums)
        # for key in nums:
        #     if count[key] > len(nums) // 3:
        #         res.add(key)
        # return list(res)

        # HashMap ~~ Counter
        map = defaultdict(int)
        res = []
        for num in nums:
            map[num] += 1
        for k, v in map.items():
            if v > len(nums) // 3:
                res.append(k)
        return res        