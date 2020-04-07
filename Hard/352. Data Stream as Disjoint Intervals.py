import bisect
class SummaryRanges:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stream = []
        

    def addNum(self, val: int) -> None:
        left = bisect.bisect_left(self.stream, [val])
        right = bisect.bisect_right(self.stream, [val])
        if left == 0:
            self.stream.insert(0, [val,val])
        elif right == len(self.stream):
            self.stream.append([val,val])
        else:
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

    def getIntervals(self) -> list:
        return self.stream
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()