class Solution:
    def merge(self, intervals: list) -> list:
        if not intervals: return intervals
    
        intervals.sort()
        
        index = 0
        while index < len(intervals)-1:
            pre = intervals[index]
            cur = intervals[index+1]
            
            if pre[1] >= cur[0]:
                if cur[1] >= pre[1]:
                    pre[1] = cur[1]
                    intervals.pop(index+1)
                else:
                    intervals.pop(index+1)
            else:
                index += 1
        return intervals