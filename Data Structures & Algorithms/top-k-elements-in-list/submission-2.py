
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            map[num] = 1 + map.get(num, 0)
        
        # return [key for key,_ in sorted(map.items(), key=lambda x:x[1], reverse=True)[:k]]
      
        for n, c in map.items():
            bucket[c].append(n)
        
        res = []

        for i in range(len(bucket) - 1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res