class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, res

        while l <= r:
            mid = (l+r)//2
            need = 0
            for pile in piles:
                need += math.ceil(pile/mid)
            if need <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res