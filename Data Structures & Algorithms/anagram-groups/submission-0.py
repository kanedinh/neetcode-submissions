from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        res = []

        for s in strs:
            sortedS = tuple(sorted(s))
            hashMap[sortedS].append(s)
        
        for val in hashMap.values():
            res.append(val)
        return res

        return list(hashMap.values())