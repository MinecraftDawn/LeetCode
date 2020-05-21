class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i in range(len(s)):
            char = s[i]
            if char in chars:
                chars[char] = [i,False]
            else:
                chars[char] = [i,True]

        ans = float("inf")
        for k,v in chars.items():
            if v[1]:
                ans = min(ans, v[0])

        return  ans if ans != float("inf") else -1


s = "loveleetcode"
ans = Solution().firstUniqChar(s)
print(ans)