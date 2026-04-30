class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = [] # [end, numPass]
        trips.sort(key=lambda x:x[1])
        curPass = 0

        for numPassenger, start, end in trips:
            # end <= start -> pop
            while minHeap and minHeap[0][0] <= start:
                _, numPass = heapq.heappop(minHeap)
                curPass -= numPass
            # push
            heapq.heappush(minHeap, [end, numPassenger])
            curPass += numPassenger
            if curPass > capacity:
                return False
        return True