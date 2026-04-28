from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(list)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in map.keys():
                return [map[diff][0], i]
            map[nums[i]].append(i)
        # print(map)