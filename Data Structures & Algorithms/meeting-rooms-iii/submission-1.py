class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        # two minHeap: used & available
        used = [] # (end, room_number)
        available = [i for i in range(n)] # room_number: 0 -> n - 1
        heapq.heapify(available)
        count = [0] * n # count the use of each room

        for start, end in meetings:
            # finish the meetings
            while used and used[0][0] <= start:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # no room is available
            if not available:
                endTime, room = heapq.heappop(used)
                end = endTime + (end - start)
                heapq.heappush(available, room)

            # a room is available
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))