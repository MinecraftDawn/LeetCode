from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        odd = False

        for k,v in counter.items():
            ans += v // 2 * 2
            if v % 2:
                odd = True
        if odd: ans += 1

        return ans