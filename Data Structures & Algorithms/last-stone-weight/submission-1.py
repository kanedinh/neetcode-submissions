class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxHeap
        res = 0
        maxHeap = []
        
        maxHeap = [-x for x in stones]
        # print(maxHeap)
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue
            else:
                remain = abs(x) - abs(y)
                heapq.heappush(maxHeap, -remain)

        return abs(maxHeap[0]) if maxHeap else 0