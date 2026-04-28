class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people) - 1
        count = 0
        
        while l <= r:
            if l == r:
                count += 1
                return count
            w = people[l] + people[r]
            if w <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                count += 1
                r -= 1
        return count