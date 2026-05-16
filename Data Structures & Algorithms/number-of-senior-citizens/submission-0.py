class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def get_age(s):
            return int(s[11:13])
        cnt = 0
        for s in details:
            if get_age(s) > 60:
                cnt += 1
        return cnt