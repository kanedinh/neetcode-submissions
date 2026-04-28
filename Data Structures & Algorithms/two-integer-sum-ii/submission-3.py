class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     for j in range(i + 1, len(numbers)):
        #         if diff == numbers[j]:
        #             return [i + 1, j + 1]
        
        l, r = 0, len(numbers) - 1

        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l + 1, r + 1]
            elif res > target:
                r -= 1
            else:
                l += 1
        return [l, r]