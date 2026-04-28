class Twitter:

    def __init__(self):
        self.time = 0 # the time post tweet
        self.tweetMap = collections.defaultdict(list) # 'userId':[time, tweetId]
        self.followingId = collections.defaultdict(set) # 'userId':set(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followingId[userId].add(userId)
        for following in self.followingId[userId]:
            if following in self.tweetMap:
                idx = len(self.tweetMap[following])
                time, tweetId = self.tweetMap[following][idx - 1]
                minHeap.append([time, tweetId, following, idx - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            time, tweetId, following, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx > 0:
                time, tweetId = self.tweetMap[following][idx - 1]
                heapq.heappush(minHeap, [time, tweetId, following, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followingId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followingId[followerId]:
            self.followingId[followerId].remove(followeeId)