class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenW = len(s1)
        l = 0
        r = l + lenW - 1
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