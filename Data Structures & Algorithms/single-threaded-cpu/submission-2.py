class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # available = []
        # pending = []
        # res = []
        # time = 0

        # for i, [enqueueTime, processTime] in enumerate(tasks):
        #     pending.append([enqueueTime, processTime, i])

        # heapq.heapify(pending)
        
        # while available or pending:
        #     while pending and pending[0][0] <= time:
        #         enqueueTime, processTime, idx = heapq.heappop(pending)
        #         heapq.heappush(available, [processTime, idx])
            
        #     if not available:
        #         time = pending[0][0]
        #         continue
            
        #     processTime, idx = heapq.heappop(available)
        #     time += processTime
        #     res.append(idx)

        # return res

        res = []
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t: t[0])

        res, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            if not minHeap:
                time = tasks[i][0]
                continue
            processTime, idx = heapq.heappop(minHeap)
            time += processTime
            res.append(idx)
        return res