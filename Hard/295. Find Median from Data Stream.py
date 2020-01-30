import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stream = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.stream, num)

    def findMedian(self) -> float:
        mid = len(self.stream) // 2
        if len(self.stream) % 2:
            return self.stream[mid]
        else:
            return (self.stream[mid-1] + self.stream[mid]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()