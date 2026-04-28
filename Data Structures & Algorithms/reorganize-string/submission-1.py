class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, c] for c, cnt in count.items()]
        res = ""
        prev = None
        heapq.heapify(maxHeap)

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, c = heapq.heappop(maxHeap)
            cnt += 1
            res += c

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if cnt != 0:
                prev = [cnt, c]
        return res