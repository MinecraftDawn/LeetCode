import bisect
class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stream = [[float('-inf'),float('-inf')],
                       [float('inf'),float('inf')]]
        

    def addNum(self, val: int) -> None:
        left = bisect.bisect_left(self.stream, [val])
        right = bisect.bisect_right(self.stream, [val])
        flag = 0
        if self.stream[left-1][1] == val-1:
            self.stream[left-1][1] = val
            flag += 1
        
        if self.stream[right][0] == val+1:
            self.stream[right][0] = val
            flag += 1

        if flag == 2:
            self.stream[left-1][1] = self.stream[right][1]
            self.stream.pop(right)
        elif flag == 0:
            bisect.insort_left(self.stream, [val,val])

    def getIntervals(self) -> list:
        return self.stream[1:-1]
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()