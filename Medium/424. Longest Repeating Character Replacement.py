from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        left = 0
        right = 0
        ans = 0
        curMax = 0

        while right < len(s):
            char = s[right]
            chars[char] += 1
            curMax = max(curMax, chars[char])

            if right - left + 1 - curMax > k:
                ans = max(ans, right - left)
                chars[s[left]] -= 1
                left += 1

            right += 1

        return max(ans, right-left)