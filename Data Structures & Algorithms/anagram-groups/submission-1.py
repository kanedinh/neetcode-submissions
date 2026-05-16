class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            hashMap[sorted_s].append(s)
        
        # for val in hashMap.values():
        #     res.append(val)
        # return res

        return list(hashMap.values())