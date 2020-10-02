class Solution:
    def findRightInterval(self, intervals: list) -> list:
        intervals = [x + [i] for i, x in enumerate(intervals)]
        ans = [0] * len(intervals)

        intervals.sort()

        for i in range(len(intervals)):
            index = intervals[i][2]
            found = self.binarySearch(intervals, intervals[i][1], i)

            if found < len(intervals) and i != found and intervals[found][0] >= intervals[i][1]:
                ans[index] = intervals[found][2]
            else:
                ans[index] = -1

        return ans

    def binarySearch(self, intervals: list, target: int, left: int):
        left += 1
        right = len(intervals) - 1

        while left < right:
            mid = (left + right) // 2
            midVal = intervals[mid][0]

            if target < midVal:
                right = mid
            elif target > midVal:
                left = mid + 1
            else:
                return mid

        return left