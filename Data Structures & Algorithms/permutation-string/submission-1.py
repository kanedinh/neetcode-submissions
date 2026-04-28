class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n > m: return False
        
        l = 0
        r = l + n - 1
        mp = {}
        for s in s1:
            mp[s] = 1 + mp.get(s, 0)
        while r < len(s2):
            tmp = {}
            window = s2[l:r+1]
            for s in window:
                tmp[s] = 1 + tmp.get(s, 0)
            if tmp == mp:
                return True
            l += 1
            r += 1
        return False