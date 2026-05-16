class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        numAppend = 0
        i = 0
        if not t:
            return 0
        for c in s:
            if c == t[i]:
                i += 1
            if i >= len(t):
                break
        return len(t) - i