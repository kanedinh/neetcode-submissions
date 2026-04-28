class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in count.items()]
        prev = None
        heapq.heapify(maxHeap)
        res = ""

        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            
            cnt, c = heapq.heappop(maxHeap)
            res += c
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, c]
        return res