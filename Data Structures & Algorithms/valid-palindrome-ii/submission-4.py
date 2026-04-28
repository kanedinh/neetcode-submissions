class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                l, r = s[i + 1: j + 1], s[i:j]
                return (l == l[::-1] or r == r[::-1])
            i += 1
            j -= 1
        return True