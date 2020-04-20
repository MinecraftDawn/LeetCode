from collections import defaultdict, deque
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.follings = defaultdict(set)
        self.post = defaultdict(deque)
        self.history = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        posts = self.post[userId]
        posts.append(tweetId)
        if len(posts) > 10: posts.popleft()
        
        self.history[tweetId] = self.time
        self.time += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        self.follings[userId].add(userId)
        
        posts = []
        for follower in self.follings[userId]:
            posts.extend(self.post[follower])
            
        return sorted(posts, key=lambda x: self.history[x], reverse=True)[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.follings[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)