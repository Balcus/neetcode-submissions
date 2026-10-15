class Twitter:

    """
    3 attributes:
    tweets: hash_map, maps userIds to the tweets they posted as well as the post time
    we want a list for the value instead of a hashmap because tweets[userId][-1] will always return the latest tweet the user posted, set does not guarantee ordering
    { userId: [(time, tweetId)] }

    follow: hash_map, maps userId to followeeId, who does each user follow
    { userId: (followeeId1, followeeId2) }

    time: used to order the tweets
    """
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    # Time Complexity: O(1)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    # Time Complexity: O(f + klogf), in our case k = 10
    def getNewsFeed(self, userId: int) -> list[int]:
        res = [] # ordered from the most recent tweet
        minHeap = []

        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if not followeeId in self.tweets:
                continue

            idx = len(self.tweets[followeeId]) - 1
            time, tweetId = self.tweets[followeeId][idx]

            # this is horrible, uses the solution for k sorted list (that is the reason why we need the idx)
            minHeap.append([time, tweetId, followeeId, idx - 1])

        heapq.heapify(minHeap) # O(f) where f is the number of followers the user has

        # max k iterations, on each the pop/push costs O(logf) where f is the number of followers
        while minHeap and len(res) < 10:
            time, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)

            if idx < 0:
                continue

            time, tweetId = self.tweets[followeeId][idx]
            heapq.heappush(minHeap, [time, tweetId, followeeId, idx - 1])

        return res

    # Time Complexity: O(1)
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    # Time Complexity: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)