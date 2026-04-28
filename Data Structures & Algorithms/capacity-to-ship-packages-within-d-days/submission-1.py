class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ship, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ship += 1
                    currCap = cap
                currCap -= w
            return ship <= days
        
        while l <= r:
            mid = (l+r)//2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res
            