class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

        # 1 2 0 1 0
        # goal = 4
        # i: 3 -> 3 + 1 >= 4 -> goal = 3
        # i: 2 -> 2 + 0 < 4
        # i: 1 -> 1 + 2 >= 2 -> goal = 1
        # i: 0 -> 0 + 1 >= 1 -> goal = 0