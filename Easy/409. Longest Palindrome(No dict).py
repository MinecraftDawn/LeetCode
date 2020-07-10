class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = [0] * 52
        ans = 0
        odd = False

        for char in s:
            index = ord(char) - 65
            if index > 25: index -= 6
            counter[index] += 1

        for count in counter:
            ans += count // 2 * 2
            if count % 2:
                odd = True

        if odd: ans += 1

        return ans