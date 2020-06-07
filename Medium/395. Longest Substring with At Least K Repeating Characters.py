# Reference: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/600503/C%2B%2B-Recursive-Solution-100-Time-100-Mem
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0

        chars = [0] * 26
        count = 0

        for char in s:
            chars[ord(char) - ord('a')] += 1

        for char in s:
            if chars[ord(char) - ord('a')] >= k:
                count += 1
            else:
                left = s[:count]

                while count < len(s) and chars[ord(s[count]) - ord('a')] < k:
                    count += 1
                right = s[count:]
                print("L", left, "R", right, count)

                return max(self.longestSubstring(left, k),
                           self.longestSubstring(right, k))

        return count