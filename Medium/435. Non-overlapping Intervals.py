class Solution:
    def eraseOverlapIntervals(self, intervals: list) -> int:
        intervals.sort(key=lambda x: x[1])

        ans = 0
        pre = float("-inf")
        for start, end in intervals:
            if start >= pre:
                pre = end
            else:
                ans += 1

        return ans