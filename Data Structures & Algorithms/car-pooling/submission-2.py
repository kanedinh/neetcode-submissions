class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])

        # for i in range(len(trips)):
        #     curPass = trips[i][0]
        #     for j in range(i):
        #         if trips[j][2] > trips[i][1]:
        #             curPass += trips[j][0]
        #         if curPass > capacity:
        #             return False
        # return True

        minHeap = []
        curPass = 0
        for i in trips:
            numPass, start, end = i
            while minHeap and minHeap[0][0] <= start:
                curPass -= minHeap[0][1]
                heapq.heappop(minHeap)            
            curPass += numPass
            if curPass > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True