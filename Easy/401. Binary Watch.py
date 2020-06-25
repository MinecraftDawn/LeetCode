from itertools import combinations


class Solution:
    def readBinaryWatch(self, num: int) -> list:
        hours = [8, 4, 2, 1]
        mins = [32, 16, 8, 4, 2, 1]
        ans = []

        for i in range(num+1):
            if num - i > 6: continue

            hour = list(combinations(hours, i))
            minute = list(combinations(mins, num - i))

            for h in hour:
                h = sum(h)
                if h >= 12: continue
                for m in minute:
                    m = sum(m)
                    if m >= 60: continue
                    ans.append(str(h)+":"+str(m).zfill(2))

        return ans