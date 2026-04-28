class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        res = []
        time = 0

        for i, [enqueueTime, processTime] in enumerate(tasks):
            pending.append([enqueueTime, processTime, i])

        heapq.heapify(pending)
        
        while available or pending:
            while pending and pending[0][0] <= time:
                enqueueTime, processTime, idx = heapq.heappop(pending)
                heapq.heappush(available, [processTime, idx])
            
            if not available:
                time = pending[0][0]
                continue
            
            processTime, idx = heapq.heappop(available)
            time += processTime
            res.append(idx)

        return res