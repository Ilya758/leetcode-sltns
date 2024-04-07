from collections import defaultdict
from heapq import *


class Twitter:
    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        heap = []
        self.followers[userId].add(userId)
        
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                heappush(heap, [count, tweetId, followeeId, index - 1])

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heappop(heap)
            res.append(tweetId)
            
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heappush(heap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)