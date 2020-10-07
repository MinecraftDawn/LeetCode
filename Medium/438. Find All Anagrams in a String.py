from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        if len(s) < len(p): return []

        target = Counter(p)
        ans = []
        curCount = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            char = s[i]
            curCount[char] += 1
            if curCount == target:
                ans.append(i - len(p) + 1)

            char = s[i - len(p) + 1]
            curCount[char] -= 1
            if curCount[char] == 0:
                del curCount[char]

        return ans