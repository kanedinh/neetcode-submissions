class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        w = set()
        k = 0
        l = 0
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            k = max(k, r - l + 1)

        return k